def element_is_visible(self, locator, timeout=5):
    """
    Ожидает проверку, что элемент присутствует в DOM-дереве, виден и отображается на странице.
    Видимость означает, что элемент не только отображается,
    но также имеет высоту и ширину больше 0.
    Локатор - используется для поиска элемента. Возвращает WebElement.
    Timeout - время в течение которого он будет ожидать. По умолчанию стоит 5 секунд,
    при необходимости можно будет изменить.
    """
    self.go_to_element(self.element_is_present(locator))
    return wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))


def elements_are_visible(self, locator, timeout=5):
    """
    Ожидает проверку, что элементы присутствуют в DOM-дереве, видны и отображаются на странице.
    Видимость означает, что элементы не только отображаются,
    но также имеет высоту и ширину больше 0.
    Локатор - используется для поиска элементов. Возвращает WebElements.
    Timeout - время в течение которого он будет ожидать. По умолчанию стоит 5 секунд,
    при необходимости можно будет изменить.
    """
    return wait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))


def element_is_present(self, locator, timeout=5):
    """
    Ожидает проверку, что элемент присутствует в DOM-дереве, но не обязательно,
    что виден и отображается на странице.
    Локатор - используется для поиска элемента. Возвращает WebElement.
    Timeout - время в течение которого он будет ожидать. По умолчанию стоит 5 секунд,
    при необходимости можно будет изменить.
    """
    return wait(self.driver, timeout).until(EC.presence_of_element_located(locator))


def elements_are_present(self, locator, timeout=5):
    """
    Ожидает проверку, что элементы присутствуют в DOM-дереве, но не обязательно,
    что видны и отображаются на странице.
    Локатор - используется для поиска элемента. Возвращает WebElement.
    Timeout - время в течение которого он будет ожидать. По умолчанию стоит 5 секунд,
    при необходимости можно будет изменить.
    """
    return wait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))


def element_is_not_visible(self, locator, timeout=5):
    """
    Ожидает проверку, является ли элемент невидимым или нет. Элемент присутствует в DOM-дереве.
    Локатор - используется для поиска элемента. Возвращает WebElement.
    Timeout - время в течение которого он будет ожидать. По умолчанию стоит 5 секунд,
    при необходимости можно будет изменить.
    """
    return wait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))


def element_is_clickable(self, locator, timeout=5):
    """
    Ожидает проверку, что жлемент виден, отображается на странице,
    а также элемент включен. Элемент присутствует в DOM-дереве.
    Локатор - используется для поиска элемента.
    Timeout - время в течение которого он будет ожидать. По умолчанию стоит 5 секунд,
    при необходимости можно будет изменить.
    """
    return wait(self.driver, timeout).until(EC.element_to_be_clickable(locator))


def go_to_element(self, element):
    """
    Проскроливет страницу к выбранному элементы, так, чтобы элемент стал видимым пользователю.
    """
    self.driver.execute_script("arguments[0].scrollIntoView();", element)


def action_move_to_element(self, element):
    """
    Двигает курсор мышки на середину выбранного элемента
    Имитирует hover.
    Можно использовать для проверки интерактивности элемента при наведении
    курсора мышки на элемент.
    """
    action = ActionChains(self.driver)
    action.move_to_element(element)
    action.perform()
