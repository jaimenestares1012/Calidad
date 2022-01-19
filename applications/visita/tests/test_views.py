from audioop import reverse
from django.test import TestCase
from django.urls import reverse

# se hace la creacion de los test
class TestViews(TestCase):
    # probamos el view de registrar visita
    def test_should_show_anadir_page(self):
        response = self.client.get(reverse("add_visita"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "visita/add_visita.html")
        
    # probamos el view de ver la lista de visitas  
    # def test_should_show_lista_page(self):
    #     response = self.client.get(reverse("lista_visita"))
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, "visita/prueba.html")
