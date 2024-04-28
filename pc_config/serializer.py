import json
from rest_framework import serializers
from .models import *

class BuildSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = build
        fields = '__all__'

    def validate(self, data):
        # Extract instances of related models from the data
        cpu = data.get('CPU')
        mb = data.get('MB')
        ram = data.get('Ram')
        storage = data.get('Storage')
        gpu = data.get('GPU')
        psu = data.get('PSU')

        errors = {}  # Создаем словарь для хранения ошибок

        # Check compatibility of CPU and motherboard sockets
        if cpu and mb and cpu.socket != mb.socket:
            errors['CPU'] = "Сокеты процессора и материнской платы не совместимы."

        # Check compatibility of RAM type and motherboard
        if mb and ram and mb.DDR_Type != ram.Type:
            errors['Ram'] = "Тип оперативной памяти не подходит к материнской плате"

        # Check if motherboard supports M.2 when adding M.2 storage
        if not mb.M2_sum and storage and storage.Type == "M2":
            errors['Storage'] = "К сожалению, ваша материнская плата не поддерживает M.2 формат"

        # Check if a CPU with integrated graphics is selected along with a GPU
        if cpu.type == 'CPU' and not gpu:
            errors['GPU'] = "Вы выбрали процессор без видеоядра, вам обязательно нужно выбрать видеокарту"

        # Check if the PSU power is sufficient for the GPU
        if gpu and psu and gpu.recommend_psu > psu.power:
            errors['PSU'] = "Не хватает мощности блока питания"

        error_messages = {}
        for key, value in errors.items():
            error_messages[key] = [value]

        if errors:
            raise serializers.ValidationError(errors)  # Выбрасываем исключение с ошибками

        return data
