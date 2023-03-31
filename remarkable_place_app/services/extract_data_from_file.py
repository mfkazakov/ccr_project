from dataclasses import dataclass
from rest_framework.serializers import ValidationError
from openpyxl import load_workbook


@dataclass
class ParseResult:
    name: str
    lon: float
    lat: float
    rating: int

    def __str__(self):
        return f'ParseResult(name - {self.name}, lon - {self.lon}, lat - {self.lat}, rating - {self.rating})'


class DefaultParserFile:
    """
    Стандартный парсер из xlsx файла
    """
    def __init__(self, file):
        self.file = file

    def parse_file(self) -> list:
        try:
            wb = load_workbook(filename=self.file)
        except Exception as e:
            raise ValidationError(str(e))

        sheet_ranges = wb['Лист1']
        i = 2
        result = []
        while True:
            if (sheet_ranges[f'A{i}'].value is None or sheet_ranges[f'B{i}'].value is None
                    or sheet_ranges[f'C{i}'].value is None or sheet_ranges[f'D{i}'].value is None):     # Если хотябы одна ячейка пуста, то заканчиваем чтение файла
                break
            try:
                result.append(ParseResult(
                    name=sheet_ranges[f'A{i}'].value,
                    lon=float(sheet_ranges[f'B{i}'].value),
                    lat=float(sheet_ranges[f'C{i}'].value),
                    rating=int(sheet_ranges[f'D{i}'].value),
                ))
            except Exception as e:
                raise ValidationError(str(e))

            i += 1
        return result


class RemarkablePlacesFromFile:
    """
    Примечательные места из загруженного файла
    """
    def __init__(self, file):
        self.parser = DefaultParserFile
        self.file = file

    def get_items(self) -> list:
        data = self.parser(self.file).parse_file()
        format_data = list()
        for item in data:
            format_data.append({
                'name': item.name,
                'lon': item.lon,
                'lat': item.lat,
                'rating': item.rating
            })
        return format_data

