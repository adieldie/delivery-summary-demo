import unittest
from summary import calcular_resumo
class Tests(unittest.TestCase):
 def row(self,**kw): return dict(motoboy='Exemplo',taxa=5,pagavel=True,bairro='Fictício',bairro_cadastrado=True,**kw)
 def test_empty(self): self.assertEqual(calcular_resumo([])['total'],0)
 def test_summary(self):
  r=calcular_resumo([self.row(),self.row()]);self.assertEqual(r['total'],10);self.assertEqual(r['qtd_5'],2)
 def test_not_payable(self):
  row=self.row();row['pagavel']=False;r=calcular_resumo([row]);self.assertEqual(r['total'],0);self.assertEqual(r['pedidos_no_extrato'],1)
 def test_unknown_area(self):
  row=self.row();row['bairro_cadastrado']=False;self.assertEqual(calcular_resumo([row])['bairros_nao_cadastrados'],['Fictício'])
if __name__=='__main__': unittest.main()
