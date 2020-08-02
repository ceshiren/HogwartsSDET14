from selenium.webdriver.common.by import By


def handle_black(func):
    def wrapper(*args, **kwargs):
        _black_list = [
            (By.XPATH, "//*[@resource-id='com.xueqiu.android:id/iv_close']")
        ]
        from xueqiu_app.page.base_page import BasePage
        instance: BasePage = args[0]
        try:
            element = func(*args, **kwargs)
            _error_num = 0
            instance.set_implicitly_wait(3)
            return element
        except Exception as e:
            instance.set_implicitly_wait(1)
            # 如果没找到，就进行黑名单处理
            if instance._error_num > instance._max_err_num:
                # 如果 erro 次数大于指定指，清空 error 次数并报异常
                instance._error_num = 0
                raise e
            instance._error_num += 1
            for ele in instance._black_list:
                # 对黑名单进行点击
                eles = instance.finds(ele)
                if len(eles) > 0:
                    eles[0].click()
                    return wrapper(*args, **kwargs)
            raise ValueError("元素不在黑名单中")

    return wrapper
