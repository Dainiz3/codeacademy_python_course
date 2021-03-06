# def dalyba(a, b):
#     return a / b

# a = 10
# b = 5

# padalinom = dalyba(a, b)
# print(f"Dalyba: {a} / {b} = {padalinom}")

# # Dalyba: 10 / 5 = 2.0

# import logging

# def dalyba(a, b):
#     return a / b

# a = 10
# b = 5

# padalinom = dalyba(a, b)
# logging.warning(f"Dalyba: {a} / {b} = {padalinom}")

# # WARNING:root:Dalyba: 10 / 5 = 2.0

# import logging

# logging.basicConfig(level=logging.DEBUG)

# def dalyba(a, b):
#     return a / b

# a = 10
# b = 5

# padalinom = dalyba(a, b)

# logging.debug(f"Dalyba: {a} / {b} = {padalinom}")

# # DEBUG:root:Dalyba: 10 / 5 = 2.0

# import logging

# logging.basicConfig(filename='aritmetika.log', level=logging.DEBUG)

# def dalyba(a, b):
#     return a / b

# a = 10
# b = 5
# padalinom = dalyba(a, b)

# logging.debug(f"Dalyba: {a} / {b} = {padalinom}")

# import logging

# logging.basicConfig(filename='aritmetika.log', level=logging.DEBUG, format='%(asctime)s:%(levelname)s:%(message)s')

# def dalyba(a, b):
#     return a / b

# a = 10
# b = 5

# padalinom = dalyba(a, b)
# logging.debug(f"Dalyba: {a} / {b} = {padalinom}")

# import logging

# logging.basicConfig(filename='asmenys.log', level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')

# class Asmuo:

#     def __init__(self, vardas, pavarde):
#         self.vardas = vardas
#         self.pavarde = pavarde
#         logging.info(f"Sukurtas darbuotojas: {self.vardas} {self.pavarde}")

# tomas = Asmuo("Tomas", "Kucinskas")
# rokas = Asmuo("Rokas", "Radzevicius")

# import logging
# import log_asmenys

# logging.basicConfig(filename='aritmetika.log', level=logging.DEBUG, format='%(asctime)s:%(levelname)s:%(name)s:%(message)s')

# def dalyba(a, b):
#     return a / b

# a = 10
# b = 5

# padalinom = dalyba(a, b)
# logging.debug(f"Dalyba: {a} / {b} = {padalinom}")

# import logging
# logger = logging.getLogger(__name__)
# file_handler = logging.FileHandler('aritmetika.log')
# logger.addHandler(file_handler)

# logger.setLevel(logging.DEBUG)

# formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:%(message)s')
# file_handler.setFormatter(formatter)

# def dalyba(a, b):
#     return a / b

# a = 10
# b = 5

# padalinom = dalyba(a, b)
# logger.info(f"Dalyba: {a} / {b} = {padalinom}")

# import logging

# logger = logging.getLogger(__name__)
# file_handler = logging.FileHandler('asmenys.log')
# logger.addHandler(file_handler)
# logger.setLevel(logging.DEBUG)
# formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:%(message)s')
# file_handler.setFormatter(formatter)

# class Asmuo:

#     def __init__(self, vardas, pavarde):
#         self.vardas = vardas
#         self.pavarde = pavarde
#         logger.info(f"Sukurtas darbuotojas: {self.vardas} {self.pavarde}")

# tadas = Asmuo("Tomas", "Kucinskas")
# rokas = Asmuo("Rokas", "Radzevicius")

import logging
logger = logging.getLogger(__name__)
file_handler = logging.FileHandler('aritmetika.log')
logger.addHandler(file_handler)

logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:%(message)s')
file_handler.setFormatter(formatter)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)

def dalyba(a, b):
    return a / b

a = 10
b = 5

padalinom = dalyba(a, b)
logger.info(f"Dalyba: {a} / {b} = {padalinom}")