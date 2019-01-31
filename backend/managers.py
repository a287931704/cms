from django.db import models

'''用户类型表操作'''


# class UserTypeManager(models.Manager):
#     def insert_user_type(self, user_type):
#         self.create(user_type=user_type)
#
#     def insert_type_name(self, type_name):
#         self.create(type_name=type_name)
#
#     def insert_type_desc(self, type_desc):
#         self.create(type_desc=type_desc)
#
#     def get_objects(self, user_type_id):  # 根据user_type得到一条数据
#         return self.get(user_type_id=user_type_id)


'''用户信息表操作'''


class UserInfoManager(models.Manager):
    def insert_user(self, username, password, email, phone, status):
        self.create(username=username, password=password, email=email, phone=phone, status=status)

    def query_user(self, username, password):
        return self.filter(username__exact=username, password__exact=password).count()


'''部门表操作'''


class DepInfoManager(models.Manager):
    def insert_project(self, **kwargs):
        self.create(**kwargs)

    def update_project(self, id, **kwargs):  # 如此update_time才会自动更新！！
        obj = self.get(id=id)
        obj.department_name = kwargs.get('department_name')
        obj.status = kwargs.get('status')
        obj.comments = kwargs.get('comments')
        obj.save()

    def get_pro_name(self, dep_name, type=True, id=None):
        if type:
            return self.filter(department_name__exact=dep_name).count()
        else:
            if id is not None:
                return self.get(id=id).department_name
            return self.get(department_name__exact=dep_name)

    def get_pro_info(self, type=True):
        if type:
            return self.all().values('department_name')
        else:
            return self.all()


'''职级表操作'''


class RankInfoManager(models.Manager):
    def insert_module(self, **kwargs):
        self.create(**kwargs)

    def update_rank(self, id, **kwargs):
        obj = self.get(id=id)
        obj.rank_name = kwargs.get('rank_name')
        obj.status = kwargs.get('status')
        obj.comments = kwargs.get('comments')

        obj.save()

    def get_module_name(self, rank_name, type=True, id=None):
        if type:
            return self.filter(module_name__exact=rank_name).count()
        else:
            if id is not None:
                return self.get(id=id).rank_name
            else:
                return self.get(id=rank_name)



'''员工信息表操作'''


class EmployeeInfoManager(models.Manager):
    def insert_case(self, belong_module, **kwargs):
        case_info = kwargs.get('test').pop('case_info')
        self.create(name=kwargs.get('test').get('name'), belong_project=case_info.pop('project'),
                    belong_module=belong_module,
                    author=case_info.pop('author'), include=case_info.pop('include'), request=kwargs)

    def update_case(self, belong_module, **kwargs):
        case_info = kwargs.get('test').pop('case_info')
        obj = self.get(id=case_info.pop('test_index'))
        obj.belong_project = case_info.pop('project')
        obj.belong_module = belong_module
        obj.name = kwargs.get('test').get('name')
        obj.author = case_info.pop('author')
        obj.include = case_info.pop('include')
        obj.request = kwargs
        obj.save()

    def insert_config(self, belong_module, **kwargs):
        config_info = kwargs.get('config').pop('config_info')
        self.create(name=kwargs.get('config').get('name'), belong_project=config_info.pop('project'),
                    belong_module=belong_module,
                    author=config_info.pop('author'), type=2, request=kwargs)

    def update_config(self, belong_module, **kwargs):
        config_info = kwargs.get('config').pop('config_info')
        obj = self.get(id=config_info.pop('test_index'))
        obj.belong_module = belong_module
        obj.belong_project = config_info.pop('project')
        obj.name = kwargs.get('config').get('name')
        obj.author = config_info.pop('author')
        obj.request = kwargs
        obj.save()

    def get_case_name(self, name, module_name, belong_project):
        return self.filter(belong_module__id=module_name).filter(name__exact=name).filter(
            belong_project__exact=belong_project).count()

    def get_case_by_id(self, index, type=True):
        if type:
            return self.filter(id=index).all()
        else:
            return self.get(id=index).name


'''环境变量管理'''


class EnvInfoManager(models.Manager):
    def insert_env(self, **kwargs):
        self.create(**kwargs)

    def update_env(self, index, **kwargs):
        obj = self.get(id=index)
        obj.env_name = kwargs.pop('env_name')
        obj.base_url = kwargs.pop('base_url')
        obj.simple_desc = kwargs.pop('simple_desc')
        obj.save()

    def get_env_name(self, index):
        return self.get(id=index).env_name

    def delete_env(self, index):
        self.get(id=index).delete()
