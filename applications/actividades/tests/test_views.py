from audioop import reverse
from django.test import TestCase
from django.urls import reverse

# se hace la creacion de los test
class TestViewsActividades(TestCase):
    # probamos el view de registrar visita
    def test_should_show__page_act(self):
        response = self.client.get(reverse("lista-actividades"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "actividades/lista_actividades.html")
        
    # probamos el view de ver la lista de visitas  
    def test_should_show_lista_page_act(self):
        response = self.client.get(reverse("mis-actividades"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "actividades/mis_actividades.html")
