# Вспомогательные классы для работы функций
class Order:
    def __init__(self, amount, weight, delivery_type="courier"):
        self.amount = amount
        self.weight = weight
        self.delivery_type = delivery_type


class Customer:
    def __init__(self, is_vip=False, is_new=False):
        self.is_vip = is_vip
        self.is_new = is_new


class Address:
    def __init__(self, is_remote=False):
        self.is_remote = is_remote


# Часть 1: Создание исходной функции
def calculate_delivery_cost_v1(order, customer, address):
    if order is not None:
        if address is not None:
            if order.weight > 0:
                if order.weight <= 50:
                    if order.amount >= 1000:
                        cost = 0
                        if order.delivery_type == "pickup":
                            cost = 0
                            return {"success": True, "cost": cost, "message": "Успешно"}
                        else:
                            if order.delivery_type == "courier":
                                if order.weight < 5:
                                    cost = 300
                                elif order.weight <= 10:
                                    cost = 500
                                else:
                                    cost = 500 + (order.weight - 10) * 50
                            elif order.delivery_type == "region":
                                cost = 1000 + order.weight * 100

                            if order.amount >= 10000:
                                if not address.is_remote:
                                    cost = 0
                                    return {"success": True, "cost": cost,
                                            "message": "Успешно (Бесплатная доставка от 10000)"}

                            if customer.is_vip:
                                if order.amount >= 5000:
                                    cost = 0
                                    return {"success": True, "cost": cost, "message": "Успешно (VIP)"}

                            if customer.is_new:
                                cost = cost * 0.85

                            if address.is_remote:
                                cost = cost * 1.20

                            return {"success": True, "cost": cost, "message": "Успешно"}
                    else:
                        return {"success": False, "cost": 0, "message": "Минимальная стоимость заказа 1000 рублей"}
                else:
                    return {"success": False, "cost": 0, "message": "Максимальный вес 50 кг"}
            else:
                return {"success": False, "cost": 0, "message": "Вес должен быть положительным"}
        else:
            return {"success": False, "cost": 0, "message": "Адрес не указан"}
    else:
        return {"success": False, "cost": 0, "message": "Заказ не существует"}


# Часть 2: Рефакторинг с использованием Guard Clauses
def calculate_delivery_cost_v2(order, customer, address):
    if order is None:
        return {"success": False, "cost": 0, "message": "Заказ не существует"}

    if address is None:
        return {"success": False, "cost": 0, "message": "Адрес не указан"}

    if order.weight <= 0:
        return {"success": False, "cost": 0, "message": "Вес должен быть положительным"}

    if order.weight > 50:
        return {"success": False, "cost": 0, "message": "Максимальный вес 50 кг"}

    if order.amount < 1000:
        return {"success": False, "cost": 0, "message": "Минимальная стоимость заказа 1000 рублей"}

    if order.delivery_type == "pickup":
        return {"success": True, "cost": 0, "message": "Успешно"}

    if customer.is_vip and order.amount >= 5000:
        return {"success": True, "cost": 0, "message": "Успешно (VIP)"}

    if order.amount >= 10000 and not address.is_remote:
        return {"success": True, "cost": 0, "message": "Успешно (Бесплатная доставка от 10000)"}

    cost = 0
    if order.delivery_type == "courier":
        if order.weight < 5:
            cost = 300
        elif order.weight <= 10:
            cost = 500
        else:
            cost = 500 + (order.weight - 10) * 50
    elif order.delivery_type == "region":
        cost = 1000 + order.weight * 100

    if customer.is_new:
        cost *= 0.85

    if address.is_remote:
        cost *= 1.20

    return {"success": True, "cost": cost, "message": "Успешно"}


# Часть 3: Объединение условий
def calculate_delivery_cost(order, customer, address):
    if not order or not address:
        return {"success": False, "cost": 0, "message": "Заказ и адрес доставки должны быть указаны"}

    if not (0 < order.weight <= 50):
        return {"success": False, "cost": 0, "message": "Недопустимый вес заказа (должен быть > 0 и <= 50 кг)"}

    if order.amount < 1000:
        return {"success": False, "cost": 0, "message": "Минимальная стоимость заказа 1000 рублей"}

    if order.delivery_type == "pickup" or \
            (customer.is_vip and order.amount >= 5000) or \
            (order.amount >= 10000 and not address.is_remote):
        return {"success": True, "cost": 0, "message": "Бесплатная доставка"}

    cost = 0
    if order.delivery_type == "courier":
        if order.weight < 5:
            cost = 300
        elif order.weight <= 10:
            cost = 500
        else:
            cost = 500 + (order.weight - 10) * 50
    elif order.delivery_type == "region":
        cost = 1000 + order.weight * 100

    if customer.is_new:
        cost *= 0.85

    if address.is_remote:
        cost *= 1.20

    return {"success": True, "cost": cost, "message": "Успешно"}


# Тестовые сценарии для проверки
if __name__ == "__main__":
    print("--- Запуск тестов для финальной функции (Часть 3) ---")

    # Заказ с нулевым весом -> ошибка
    print("Тест 1 (нулевой вес):", calculate_delivery_cost(Order(1500, 0), Customer(), Address()))

    # Самовывоз -> стоимость 0
    print("Тест 2 (самовывоз):", calculate_delivery_cost(Order(1500, 2, "pickup"), Customer(), Address()))

    # VIP-клиент с заказом от 5000 рублей -> бесплатная доставка
    print("Тест 3 (VIP от 5000):", calculate_delivery_cost(Order(6000, 5), Customer(is_vip=True), Address()))

    # Новый клиент -> скидка 15% (Вес 2 кг, курьер 300 * 0.85 = 255)
    print("Тест 4 (Новый клиент):", calculate_delivery_cost(Order(2000, 2), Customer(is_new=True), Address()))

    # Отдаленный регион -> наценка 20% (Регион 1000 + 12*100 = 2200, 2200 * 1.2 = 2640)
    print("Тест 5 (Отдаленный регион):",
          calculate_delivery_cost(Order(2000, 12, "region"), Customer(), Address(is_remote=True)))

    # Заказ от 10000 рублей в неотдаленный регион -> бесплатная доставка
    print("Тест 6 (От 10000, не удаленный):",
          calculate_delivery_cost(Order(11000, 5), Customer(), Address(is_remote=False)))

    # Вес более 50 кг -> ошибка
    print("Тест 7 (> 50 кг):", calculate_delivery_cost(Order(2000, 55), Customer(), Address()))

    # Заказ менее 1000 рублей -> ошибка
    print("Тест 8 (< 1000 рублей):", calculate_delivery_cost(Order(900, 5), Customer(), Address()))
