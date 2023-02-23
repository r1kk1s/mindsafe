

def get_objects_from_model(Model, **field):
    """Возвращает отфильтрованные объекты или все объекты из модели"""
    if not field:
        return Model.objects.all()
    return Model.objects.filter(**field)