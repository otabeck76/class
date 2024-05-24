class Company:
    def init(self):
        self.properties = {}

    def create_property(self, property_id, details):
        self.properties[property_id] = details

    def read_property(self, property_id):
        return self.properties.get(property_id)

    def update_property(self, property_id, new_details):
        if property_id in self.properties:
            self.properties[property_id] = new_details
        else:
            print("Property not found.")

    def delete_property(self, property_id):
        if property_id in self.properties:
            del self.properties[property_id]
        else:
            print("Property not found.")

class Company1(Company):
    def init(self):
        super().init()

    def add_others(self, property_id, designer, frontend, backend):
        if property_id in self.properties:
            self.properties[property_id]['designer'] = designer
            self.properties[property_id]['frontend'] = frontend
            self.properties[property_id]['backend'] = backend

class Company2(Company):
    def init(self):
        super().init()

    def add_others(self, property_id, designer, frontend, backend, manager, administrator):
        if property_id in self.properties:
            self.properties[property_id]['designer'] = designer
            self.properties[property_id]['frontend'] = frontend
            self.properties[property_id]['backend'] = backend
            self.properties[property_id]['manager'] = manager
            self.properties[property_id]['administrator'] = administrator

pro_sys=Company()
second_pro_sys_=Company1()
pro_sys.create_property(1,{'address':'islam K.'})
second_pro_sys_.add_others(1,'steve',33,'1991-04-30')
print(pro_sys.read_property(1))
pro_sys.update_property(1,{'adresss':'shayhontohur tumani'})
print(pro_sys.read_property(1))
pro_sys.delete_property(1)
print(pro_sys.read_property(1))

