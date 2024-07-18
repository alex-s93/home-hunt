from enum import Enum


class ApartmentTypes(Enum):
    HOTEL = "Hotel"
    HOUSE = "House"
    APARTMENT = "Apartment"
    FLAT = "Flat"
    HOSTEL = "Hostel"
    GUEST_HOUSE = "Guest house"

    @classmethod
    def choices(cls):
        return [(attr.value, attr.value) for attr in cls]
