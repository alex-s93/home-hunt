from enum import Enum


class Lands(Enum):
    BADEN_WUERTTEMBERG = "Baden-Württemberg"
    BAVARIA = "Bayern"
    BERLIN = "Berlin"
    BRANDENBURG = "Brandenburg"
    BREMEN = "Bremen"
    HAMBURG = "Hamburg"
    HESSE = "Hessen"
    LOWER_SAXONY = "Niedersachsen"
    MECKLENBURG_VORPOMMERN = "Mecklenburg-Vorpommern"
    NORTH_RHINE_WESTPHALIA = "Nordrhein-Westfalen"
    RHINELAND_PALATINATE = "Rheinland-Pfalz"
    SAARLAND = "Saarland"
    SAXONY = "Sachsen"
    SAXONY_ANHALT = "Sachsen-Anhalt"
    SCHLESWIG_HOLSTEIN = "Schleswig-Holstein"
    THURINGIA = "Thüringen"

    @classmethod
    def choices(cls):
        return [(attr.name, attr.value) for attr in cls]
