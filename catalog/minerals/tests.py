from django.urls import reverse
from django.test import TestCase

from .models import Mineral

class MineralModelTests(TestCase):
    def test_mineral_cretion(self):
        mineral = Mineral.objects.create(
            name = "Zinc",
            image_filename = "Zinc.jpg",
            image_caption = "Zinc fragment sublimed and 1cm3 cube",
            formula = "Zn",
            crystal_system = "tetragonal",
            color = "grey silver white",
            mohs_scale_hardness = "2.5",
            specific_gravity = "6.9-7.3",
            group = "Metales de transición"  
        )
        pk_mineral = mineral.pk
        self.assertEqual(Mineral.objects.filter(pk=pk_mineral).exists(), True)

class MineralViewsTests(TestCase):
    def setUp(self):
        self.mineral = Mineral.objects.create(
            name = "Lutecio",
            image_filename = "Lutecio.jpg",
            image_caption = "Lutetium sublimed dendritic and 1cm3 cube",
            formula = "Lu",
            crystal_system = "tetragonal",
            color = "silver",
            specific_gravity = "6.9-7.3",
            group = "Lantánidos"  
        )
        self.mineral2 = Mineral.objects.create(
            name = "Boro",
            image_filename = "Boro.jpg",
            image_caption = "Boro fragment sublimed and 1cm3 cube",
            formula = "Br",
            crystal_system = "tetragonal",
            color = "grey silver white",
            mohs_scale_hardness = "2.5",
            specific_gravity = "6.9-7.3",
            group = "Metales de transición"  
        )
    
    def test_mineral_list_view(self):
        resp = self.client.get(reverse('minerals:index'))
        self.assertEqual(resp.status_code, 200)
        self.assertIn(self.mineral, resp.context['minerals'])
        self.assertIn(self.mineral2, resp.context['minerals'])
        self.assertTemplateUsed(resp, 'minerals/index.html')
        self.assertContains(resp, self.mineral.name)

    def test_mineral_detail_view(self):
        resp = self.client.get(reverse('minerals:detail',
                                        kwargs={'pk': self.mineral.pk}))
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(self.mineral, resp.context['mineral'])

    def test_search_result(self):
        resp = self.client.get(reverse('minerals:search',
                                        kwargs={'term': self.mineral.name}))
        self.assertEqual(resp.status_code, 200)
