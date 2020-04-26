# -*- coding:utf-8 -*-
from crud_module import print_info
from crud_module.dao.BaseDao import BaseDao
from crud_module.domain.loginlog import Loginlog


class LoginlogDao(BaseDao):
	def __init__(self):
		super().__init__(Loginlog)
		pass


if __name__ == "__main__":
	print("123")
	loginlogDao = LoginlogDao()
	loginlog = loginlogDao.selectByPrimaryKey(1)
	# print(json.dumps(loginlog,cls=DateEncoder))
	# print(loginlog)
	print('\n'.join(['%s:%s' % item for item in loginlog.__dict__.items()]))
	print("用户名是=" + loginlog.get_user_name())

# print()json.dumps(loginlogDict , cls=DateEncoder)
