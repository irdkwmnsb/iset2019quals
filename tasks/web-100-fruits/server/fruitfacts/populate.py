from fruitfacts.db import db
from fruitfacts.config import CONFIG_FLAG

SAMPLE_COLLECTION = [
    {"name": "Apple", "cal": 130, "cal_from_fat": 0, "total_fat_g": 0.0, "total_fat_p": 0, "sodium_mg": 0,
     "sodium_p": 0, "potassium_mg": 260, "potassium_p": 7, "total_carb_g": 34, "total_carb_p": 11, "fiber_g": 5,
     "fiber_p": 20, "sugars_g": 25, "protein_g": 1, "vitamin_a_p": 2, "vitamin_c_p": 8, "calcium_p": 2, "iron_p": 2},
    {"name": "Avocado", "cal": 50, "cal_from_fat": 35, "total_fat_g": 4.5, "total_fat_p": 7, "sodium_mg": 0,
     "sodium_p": 0, "potassium_mg": 140, "potassium_p": 4, "total_carb_g": 3, "total_carb_p": 1, "fiber_g": 1,
     "fiber_p": 4, "sugars_g": 0, "protein_g": 1, "vitamin_a_p": 0, "vitamin_c_p": 4, "calcium_p": 0, "iron_p": 2},
    {"name": "Banana", "cal": 110, "cal_from_fat": 0, "total_fat_g": 0.0, "total_fat_p": 0, "sodium_mg": 0,
     "sodium_p": 0, "potassium_mg": 450, "potassium_p": 13, "total_carb_g": 30, "total_carb_p": 10, "fiber_g": 3,
     "fiber_p": 12, "sugars_g": 19, "protein_g": 1, "vitamin_a_p": 2, "vitamin_c_p": 15, "calcium_p": 0, "iron_p": 2},
    {"name": "Cantaloupe", "cal": 50, "cal_from_fat": 0, "total_fat_g": 0.0, "total_fat_p": 0, "sodium_mg": 20,
     "sodium_p": 1, "potassium_mg": 240, "potassium_p": 7, "total_carb_g": 12, "total_carb_p": 4, "fiber_g": 1,
     "fiber_p": 4, "sugars_g": 11, "protein_g": 1, "vitamin_a_p": 120, "vitamin_c_p": 80, "calcium_p": 2, "iron_p": 2},
    {"name": "Grapefruit", "cal": 60, "cal_from_fat": 0, "total_fat_g": 0.0, "total_fat_p": 0, "sodium_mg": 0,
     "sodium_p": 0, "potassium_mg": 160, "potassium_p": 5, "total_carb_g": 15, "total_carb_p": 5, "fiber_g": 2,
     "fiber_p": 8, "sugars_g": 11, "protein_g": 1, "vitamin_a_p": 35, "vitamin_c_p": 100, "calcium_p": 4, "iron_p": 0},
    {"name": "Grapes", "cal": 90, "cal_from_fat": 0, "total_fat_g": 0.0, "total_fat_p": 0, "sodium_mg": 15,
     "sodium_p": 1, "potassium_mg": 240, "potassium_p": 7, "total_carb_g": 23, "total_carb_p": 8, "fiber_g": 1,
     "fiber_p": 4, "sugars_g": 20, "protein_g": 0, "vitamin_a_p": 0, "vitamin_c_p": 2, "calcium_p": 2, "iron_p": 0},
    {"name": "Honeydew Melon", "cal": 50, "cal_from_fat": 0, "total_fat_g": 0.0, "total_fat_p": 0, "sodium_mg": 30,
     "sodium_p": 1, "potassium_mg": 210, "potassium_p": 6, "total_carb_g": 12, "total_carb_p": 4, "fiber_g": 1,
     "fiber_p": 4, "sugars_g": 11, "protein_g": 1, "vitamin_a_p": 2, "vitamin_c_p": 45, "calcium_p": 2, "iron_p": 2},
    {"name": "Kiwifruit", "cal": 90, "cal_from_fat": 10, "total_fat_g": 1.0, "total_fat_p": 2, "sodium_mg": 0,
     "sodium_p": 0, "potassium_mg": 450, "potassium_p": 13, "total_carb_g": 20, "total_carb_p": 7, "fiber_g": 4,
     "fiber_p": 16, "sugars_g": 13, "protein_g": 1, "vitamin_a_p": 2, "vitamin_c_p": 240, "calcium_p": 4, "iron_p": 2},
    {"name": "Lemon", "cal": 15, "cal_from_fat": 0, "total_fat_g": 0.0, "total_fat_p": 0, "sodium_mg": 0, "sodium_p": 0,
     "potassium_mg": 75, "potassium_p": 2, "total_carb_g": 5, "total_carb_p": 2, "fiber_g": 2, "fiber_p": 8,
     "sugars_g": 2, "protein_g": 0, "vitamin_a_p": 0, "vitamin_c_p": 40, "calcium_p": 2, "iron_p": 0},
    {"name": "Lime", "cal": 20, "cal_from_fat": 0, "total_fat_g": 0.0, "total_fat_p": 0, "sodium_mg": 0, "sodium_p": 0,
     "potassium_mg": 75, "potassium_p": 2, "total_carb_g": 7, "total_carb_p": 2, "fiber_g": 2, "fiber_p": 8,
     "sugars_g": 0, "protein_g": 0, "vitamin_a_p": 0, "vitamin_c_p": 35, "calcium_p": 0, "iron_p": 0},
    {"name": "Nectarine", "cal": 60, "cal_from_fat": 5, "total_fat_g": 0.5, "total_fat_p": 1, "sodium_mg": 0,
     "sodium_p": 0, "potassium_mg": 250, "potassium_p": 7, "total_carb_g": 15, "total_carb_p": 5, "fiber_g": 2,
     "fiber_p": 8, "sugars_g": 11, "protein_g": 1, "vitamin_a_p": 8, "vitamin_c_p": 15, "calcium_p": 0, "iron_p": 2},
    {"name": "Orange", "cal": 80, "cal_from_fat": 0, "total_fat_g": 0.0, "total_fat_p": 0, "sodium_mg": 0,
     "sodium_p": 0, "potassium_mg": 250, "potassium_p": 7, "total_carb_g": 19, "total_carb_p": 6, "fiber_g": 3,
     "fiber_p": 12, "sugars_g": 14, "protein_g": 1, "vitamin_a_p": 2, "vitamin_c_p": 130, "calcium_p": 6, "iron_p": 0},
    {"name": "Peach", "cal": 60, "cal_from_fat": 0, "total_fat_g": 0.5, "total_fat_p": 1, "sodium_mg": 0, "sodium_p": 0,
     "potassium_mg": 230, "potassium_p": 7, "total_carb_g": 15, "total_carb_p": 5, "fiber_g": 2, "fiber_p": 8,
     "sugars_g": 13, "protein_g": 1, "vitamin_a_p": 6, "vitamin_c_p": 15, "calcium_p": 0, "iron_p": 2},
    {"name": "Pear", "cal": 100, "cal_from_fat": 0, "total_fat_g": 0.0, "total_fat_p": 0, "sodium_mg": 0, "sodium_p": 0,
     "potassium_mg": 190, "potassium_p": 5, "total_carb_g": 26, "total_carb_p": 9, "fiber_g": 6, "fiber_p": 24,
     "sugars_g": 16, "protein_g": 1, "vitamin_a_p": 0, "vitamin_c_p": 10, "calcium_p": 2, "iron_p": 0},
    {"name": "Pineapple", "cal": 50, "cal_from_fat": 0, "total_fat_g": 0.0, "total_fat_p": 0, "sodium_mg": 10,
     "sodium_p": 0, "potassium_mg": 120, "potassium_p": 3, "total_carb_g": 13, "total_carb_p": 4, "fiber_g": 1,
     "fiber_p": 4, "sugars_g": 10, "protein_g": 1, "vitamin_a_p": 2, "vitamin_c_p": 50, "calcium_p": 2, "iron_p": 2},
    {"name": "Plums", "cal": 70, "cal_from_fat": 0, "total_fat_g": 0.0, "total_fat_p": 0, "sodium_mg": 0, "sodium_p": 0,
     "potassium_mg": 230, "potassium_p": 7, "total_carb_g": 19, "total_carb_p": 6, "fiber_g": 2, "fiber_p": 8,
     "sugars_g": 16, "protein_g": 1, "vitamin_a_p": 8, "vitamin_c_p": 10, "calcium_p": 0, "iron_p": 2},
    {"name": "Strawberries", "cal": 50, "cal_from_fat": 0, "total_fat_g": 0.0, "total_fat_p": 0, "sodium_mg": 0,
     "sodium_p": 0, "potassium_mg": 170, "potassium_p": 5, "total_carb_g": 11, "total_carb_p": 4, "fiber_g": 2,
     "fiber_p": 8, "sugars_g": 8, "protein_g": 1, "vitamin_a_p": 0, "vitamin_c_p": 160, "calcium_p": 2, "iron_p": 2},
    {"name": "Sweet Cherries", "cal": 100, "cal_from_fat": 0, "total_fat_g": 0.0, "total_fat_p": 0, "sodium_mg": 0,
     "sodium_p": 0, "potassium_mg": 350, "potassium_p": 10, "total_carb_g": 26, "total_carb_p": 9, "fiber_g": 1,
     "fiber_p": 4, "sugars_g": 16, "protein_g": 1, "vitamin_a_p": 2, "vitamin_c_p": 15, "calcium_p": 2, "iron_p": 2},
    {"name": "Tangerine", "cal": 50, "cal_from_fat": 0, "total_fat_g": 0.0, "total_fat_p": 0, "sodium_mg": 0,
     "sodium_p": 0, "potassium_mg": 160, "potassium_p": 5, "total_carb_g": 13, "total_carb_p": 4, "fiber_g": 2,
     "fiber_p": 8, "sugars_g": 9, "protein_g": 1, "vitamin_a_p": 6, "vitamin_c_p": 45, "calcium_p": 4, "iron_p": 0},
    {"name": "Watermelon", "cal": 80, "cal_from_fat": 0, "total_fat_g": 0.0, "total_fat_p": 0, "sodium_mg": 0,
     "sodium_p": 0, "potassium_mg": 270, "potassium_p": 8, "total_carb_g": 21, "total_carb_p": 7, "fiber_g": 1,
     "fiber_p": 4, "sugars_g": 20, "protein_g": 1, "vitamin_a_p": 30, "vitamin_c_p": 25, "calcium_p": 2, "iron_p": 4}]


def check_and_populate():
    if db["fruits"].count() == 0:
        populate()


def populate():
    db["fruits"].drop()
    db["fruits"].insert_many(SAMPLE_COLLECTION)
    db["fruits"].insert_one({"name": "The forbidden fruit", "flag": CONFIG_FLAG})


if __name__ == "__main__":
    populate()
