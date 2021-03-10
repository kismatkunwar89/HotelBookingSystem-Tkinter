import unittest
from Dashboard import Movie
import backend.database
from model.model import User



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
    def setUp(self):
        self.a=backend.database.DBConnect()

    def test_insert(self):
        """
                        Function to test if the insert works or not.
                """
        query="insert into new_table values(%s,%s,%s,%s,%s,%s,%s)"
        values=("kirtan",9818,"kkk","male",'kapan',599,"3/1/21")
        self.a.insert(query,values)
        query1="select * from new_table where name='kirtan'"
        actual=self.a.view(query1)
        self.assertEqual([("kirtan",9818,"kkk","male",'kapan',599,"3/1/21")],actual)

    def test_update(self):
        """
                Function to test if the update works or not.
        """
        query = "insert into new_table values(%s,%s,%s,%s,%s,%s,%s)"
        values = ("kirtan467", 9818, "kkk", "male" ,"kapan",511, "3/1/21")
        self.a.insert(query, values)
        query1 = "update new_table set address=%s where name=%s"
        values1 = ("maitidevi","kirtan467")
        self.a.update(query1, values1)
        query2 = "select * from new_table where name='kirtan467'"
        actual = self.a.view(query2)
        self.assertEqual([("kirtan467", 9818, "kkk", "male" ,"maitidevi",511, "3/1/21")], actual)

    def tearDown(self):
        del self.a

class Test_User(unittest.TestCase):
    """
    Class Test_User tests the User class from model.user.
    """
    def setUp(self):
        self.obj_model = User

    def test_set_rno(self):
        self.obj_model.set_rno(100)
        self.assertEqual(100, self.obj_model.get_rno())


    def tearDown(self):
        del self.obj_model



if __name__ == " __main__ ":
    unittest.main()
