from address import Address
from mailing import Mailing

to_address = Address("123456", "Москва", "Тверская", "14", "5")
from_address = Address("654321", "Санкт-Петербург", "Невский", "27", "12")
mailing = Mailing(to_address, from_address, 250, "TRK123456789")
output = (
    f"Отправление {mailing.track} из "
    f"{mailing.from_address.index}, {mailing.from_address.city}, {mailing.from_address.street}, {mailing.from_address.house} - {mailing.from_address.apartment} "
    f"в {mailing.to_address.index}, {mailing.to_address.city}, {mailing.to_address.street}, {mailing.to_address.house} - {mailing.to_address.apartment}. "
    f"Стоимость {mailing.cost} рублей."
)

print(output)