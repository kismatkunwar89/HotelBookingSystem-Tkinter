import unittest
from frontend.Dashboard import Movie
import backend.database
import model.model



class test(unittest.TestCase):
    """
       Class test tests the Functions class from fronend.Dashboard
       """
    def setUp(self):
        self.s=Movie
        self.sorted_list=[1,2,3,4,5,6]

    def test_merge_sort_text(self):
        p_text = ['Ashish', 'xeronimo', 'Bishesh', 'Prajwol', 'Bibek', 'Pandey']
        self.assertEqual([ 'Ashish','Bibek','Bishesh', 'Pandey', 'Prajwol','xeronimo'],
                         self.s.mergesort(p_text))



    def test_mergesort(self):
        num=[10,2,11,5,1]
        check=self.s.mergesort(num)
        self.assertEqual([1,2,5,10,11],check)

    def test_binarysearch(self):
        expected = '1'
        item=1
        actual = self.s.binary_room_number(self.sorted_list,item)
        self.assertNotEqual(expected, actual)




class Test_dbconect(unittest.TestCase):
    """
           Class test tests the Functions class from database.DBConnect
           """
    def setUp(self):
        self.a=backend.database.DBConnect()

    def test_insert(self):
        query = "insert into new_table values (%s,%s,%s,%s,%s,%s,%s)"
        values = ("shyamsir",9818634312, "shyamsir82@gmail.com", "male","kathmandu", 450,"3/1/21")
        self.a.insert(query, values)
        query1 = "select * from new_table where name='shyamsir'"
        actual = self.a.select(query1)
        self.assertEqual(values, actual[0])

    def test_update(self):
        query1 = "update new_table set address=%s where name=%s"
        values1 = ("kalanki", "shyamsir")
        self.a.update(query1, values1)
        query2 = "select * from new_table where name='shyamsir'"
        actual = self.a.select(query2)
        self.assertEqual(("shyamsir",9818634312, "shyamsir82@gmail.com", "male","kalanki", 450,"3/1/21"), actual[0])

    def test_delete(self):
        query = "delete from new_table where name=%s"
        value = ('shyamsir',)
        result = self.a.delete(query, value)
        self.assertEqual(None, result)


    def tearDown(self):
        del self.a

class Test_User(unittest.TestCase):
    """
    Class Test_User tests the User class from model.user.
    """
    def setUp(self):
        self.obj_model = model.model.User()

    def test_set_rno(self):
        self.obj_model.set_rno(12)
        self.assertEqual(12, self.obj_model.get_rno())

    def test_set_uname(self):
        self.obj_model.set_username("kismat")
        self.assertEqual("kismat",self.obj_model.get_username())

    def test_set_pno(self):
        self.obj_model.set_pno(9818536302)
        self.assertEqual(9818536302,self.obj_model.get_pno())


    def tearDown(self):
        del self.obj_model


if __name__ == " __main__ ":
    unittest.main()