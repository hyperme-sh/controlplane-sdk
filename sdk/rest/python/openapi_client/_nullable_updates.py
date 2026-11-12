"""Wire helpers for generated nullable update models."""


def with_explicit_nulls(model, values, nullable):
    for name, field in type(model).model_fields.items():
        wire = field.alias or name
        if wire in nullable and name in model.model_fields_set and getattr(model, name) is None:
            values[wire] = None
    return values


def restore_fields_set(model, source):
    present = {name for name, field in type(model).model_fields.items()
               if name in source or (field.alias or name) in source}
    model.model_fields_set.intersection_update(present)
    return model
