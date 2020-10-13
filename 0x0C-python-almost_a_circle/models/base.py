#!/usr/bin/python3
"""First Class Base"""


class Base:
    """Class Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes the data"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries"""
        import json
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file"""
        ls = []
        filename = "{}.json".format(cls.__name__)
        if list_objs:
            for instance in list_objs:
                ls.append(instance.to_dictionary())
        with open(filename, mode="w", encoding="utf-8") as f:
            f.write(Base.to_json_string(ls))

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation"""
        import json
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            dum = cls(1, 1)
        elif cls.__name__ == "Square":
            dum = cls(1)
        dum.update(**dictionary)
        return dum

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances"""
        filename = "{}.json".format(cls.__name__)
        try:
            with open(filename, encoding="utf-8") as f:
                ls = cls.from_json_string(f.read())
        except:
            ls = []
        ls_out = []
        for dic in ls:
            ls_out.append(cls.create(**dic))
        return ls_out

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serializes in CSV"""
        import csv
        filename = "{}.csv".format(cls.__name__)
        ls = []
        if list_objs:
            for instance in list_objs:
                ls.append(instance.to_dictionary())
        header = ls[0].keys()
        with open(filename, mode="w", newline='', encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=header)
            writer.writeheader()
            writer.writerows(ls)

    @classmethod
    def load_from_file_csv(cls):
        """Deserialized from CSV"""
        import csv
        filename = "{}.csv".format(cls.__name__)
        ls = []
        try:
            with open(filename, newline='', encoding="utf-8") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    ls.append(row)
        except:
            ls = []
        ls_out = []
        for dic in ls:
            for key in dic:
                dic[key] = int(dic[key])
        for dic in ls:
            ls_out.append(cls.create(**dic))
        return ls_out
