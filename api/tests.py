from django.test import TestCase, Client, client
from django.urls import reverse, resolve
from . import views
from projects.models import Project



# Create your tests here.

class TestURL(TestCase):
    # def test_testprojects_url(self):
    #     response = self.client.get('/api/projects/')
    #     #print(response.status_code)
    #     self.assertEqual(response.status_code, 200)
    
    def test_testprojectsurl(self):
        url = reverse('get-projects')
        #print(url) #prints the routes
        #print(resolve(url)) #resolves the url
        self.assertEqual(resolve(url).func, views.getProjects)
    
    def test_testgetroutes(self):
        url = reverse('get-routes')
        #print(url) #prints the routes
        #print(resolve(url)) #resolves the url
        self.assertEqual(resolve(url).func, views.getRoutes)
    
    def test_testgetproject(self):
        url = reverse('get-project', args=['d55789c5-07bc-44e1-bafc-363213660d6d',])
        #print(url) #prints the routes
        #print(resolve(url)) #resolves the url
        self.assertEqual(resolve(url).func, views.getProject)
    

class TestViews(TestCase):
    
    def test_getprojects_view(self):
        client = Client()
        response = client.get(reverse('get-projects'))
        #print(response)
        self.assertEqual(response.status_code, 200)
    

