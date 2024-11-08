ó
1 )gc           @   sź   d  Z  d d l Z d d l m Z d d l m Z m Z m Z d d l m Z m	 Z	 d e j
 f d     YZ d e j
 f d	     YZ d
 e j
 f d     YZ e d k r¸ e j   n  d S(   s(    A function that test the utils.py file.i˙˙˙˙N(   t   parameterized(   t   access_nested_mapt   get_jsont   memoize(   t   patcht   Mockt   TestAccessNestedMapc           B   sŤ   e  Z d  Z e j i d d 6d	 d f i i d d 6d 6d
 i d d 6f i i d d 6d 6d d f g  d    Z e j i  d d f i d d 6d d f g  d    Z RS(   ss   
    Test class for the access_nested_map function from the utils module.
    Inherits form unittest.TestCase.
    i   t   ai   t   bc         C   s   |  j  t | |  |  d S(   s0  
        Test the access-nested_map function with different imputs.
        Parameters:
        nested_map (Mapping): The nested map to access.
        path (Sequence): The sequece of keys representing the path to the
        value.
        expected (Any): The expected result from the function.
        N(   t   assertEqualR   (   t   selft
   nested_mapt   patht   expected(    (    s   test_utils.pyt   test_access_nested_map   s    s   'a's   'b'c         C   sB   |  j  t   } t | |  Wd QX|  j t | j  |  d S(   sa  
        Test the access_nested_map function to ensur it rases KeyError for
        invalid paths.

        Parameters:
        nested_map (Mapping): The nested map to access.
        path (Sequence): The sequence of keys representing the path to the
        value.
        expected_exception (str): The expected exception), expected_exception)
        N(   t   assertRaisest   KeyErrorR   R	   t   strt	   exception(   R
   R   R   t   expected_exceptiont   context(    (    s   test_utils.pyt    test_access_nested_map_exception   s    (   R   (   R   (   R   R   (   R   (   R   R   (   t   __name__t
   __module__t   __doc__R    t   expandR   R   (    (    (    s   test_utils.pyR   	   s   !,t   TestGetJsonc           B   sR   e  Z d  Z e j d i e d 6f d i e d 6f g  e d  d     Z RS(   sj   
    Test class for the get_json function from the utils module.
    Inherits from unittest.TestCase.
    s   http://example.comt   payloads   http://holberton.ios   utils.requests.getc         C   sK   t    } | | j _ | | _ t |  } t j |  |  j | |  d S(   s;  
        Test the get_json function with different inputs.

        Parameters:
        test_url (str): The URL to be passed to the get-json function.
        test_payload (dict): The expeted Json payload returned by the
        mocked requests.get.
        mock_get (Mock): The mocked requests.get method.
        N(   R   t   jsont   return_valueR   t   Mock_gett   assert_called_once_withR	   (   R
   t   test_urlt   test_payloadt   mock_gett   mock_responset   result(    (    s   test_utils.pyt   test_get_json9   s    		(	   R   R   R   R    R   t   Truet   FalseR   R%   (    (    (    s   test_utils.pyR   4   s
   t   TestMemoizec           B   s   e  Z d  Z d   Z RS(   sh   
    Test class for th memoize function from the utils module.
    Inherits form unittest.TestCase.
    c         C   s}   d d d     Y} t  j | d d d L } |   } | j } | j } | j   |  j | d  |  j | d  Wd QXd S(   sm   
        Test the memoize decorator to ensure that the decorated method is
        called only once.
        t	   TestClassc           B   s    e  Z d    Z e d    Z RS(   c         S   s   d S(   Ni*   (    (   R
   (    (    s   test_utils.pyt   a_methode   s    c         S   s
   |  j    S(   N(   R*   (   R
   (    (    s   test_utils.pyt
   a_propertyh   s    (   R   R   R*   R   R+   (    (    (    s   test_utils.pyR)   d   s   	R*   R   i*   N(    (   R   t   objectR+   t   assert_called_onceR	   (   R
   R)   t   mock_methodt   objt   res1t   res2(    (    s   test_utils.pyt   test_memoize^   s    			
(   R   R   R   R2   (    (    (    s   test_utils.pyR(   X   s   t   __main__(   R   t   unittestR    t   utilsR   R   R   t   unittest.mockR   R   t   TestCaseR   R   R(   R   t   main(    (    (    s   test_utils.pyt   <module>   s   +$$