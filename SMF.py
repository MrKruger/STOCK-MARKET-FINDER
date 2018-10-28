"""
	TITLE: STOCK MARKET FINDER
	AUTHOR: GABRIEL KRÜGER
	DATE: 28/10/18
	v1.0
"""

import os
import urllib.request
from bs4 import BeautifulSoup
import Banners_SMF 

Banners_SMF.Banners_List()

Banners_SMF.Banners_Prints_0()

try:
	Option = int(input("Option  --> "))
	
	while Option == 1 or Option == 2 or Option == 3 or Option == 4 or Option == 5 or Option == 6 or Option == 7 or Option == 8 or Option == 9:
		if Option == 1:
			print("\n")

			answer = str(input("SMF_BOT --> Qual o Ativo desejado? (Digite o código do Ativo) \nResposta -> "))

			url = 'https://www.comparandus.com.br/acao/%s' % (answer.upper())

			page = urllib.request.urlopen(url)

			soup = BeautifulSoup(page, 'html5lib')

			os.system("cls" or "clear")

			ticker = soup.find_all("td")[1].get_text()

			quotation = soup.find_all("td")[3].get_text()

			kind = soup.find_all("td")[5].get_text()

			date_last_neg = soup.find_all("td")[7].get_text()

			company = soup.find_all("td")[9].get_text()

			min_52 = soup.find_all("td")[11].get_text()

			sector = soup.find_all("td")[13].get_text()

			max_52 = soup.find_all("td")[15].get_text()

			sub_sector = soup.find_all("td")[17].get_text()

			average_vol = soup.find_all("td")[19].get_text()

			market_value = soup.find_all("td")[21].get_text()

			last_balance_sheet = soup.find_all("td")[23].get_text()

			enterprise_value = soup.find_all("td")[25].get_text()

			stock_number = soup.find_all("td")[27].get_text()

			dividend_per_stock = soup.find_all("td")[30].get_text()

			dividend_yield = soup.find_all("td")[32].get_text()

			price_profit = soup.find_all("td")[34].get_text()

			proftit_per_stock = soup.find_all("td")[36].get_text()

			equity_value = soup.find_all("td")[38].get_text()

			equity_value_per_stock = soup.find_all("td")[40].get_text()
 
			price_per_EBIT = soup.find_all("td")[42].get_text()

			gross_margin = soup.find_all("td")[44].get_text()

			price_sales_ratio = soup.find_all("td")[46].get_text()

			margin_EBIT = soup.find_all("td")[48].get_text()

			price_asset = soup.find_all("td")[50].get_text()

			net_margin = soup.find_all("td")[52].get_text()

			price_working_capital = soup.find_all("td")[54].get_text()

			EBIT_asset = soup.find_all("td")[56].get_text()

			price_liq_current_asset = soup.find_all("td")[58].get_text()

			return_on_invested_capital = soup.find_all("td")[62].get_text()

			return_on_equity = soup.find_all("td")[64].get_text()

			enterprise_value_EBIT = soup.find_all("td")[66].get_text()

			liquid_current = soup.find_all("td")[68].get_text()

			spin_asset = soup.find_all("td")[70].get_text()

			gross_debt_patrimony = soup.find_all("td")[72].get_text()

			#revenue_growth = 

			own_assets = soup.find_all("td")[74].get_text()

			gross_debt = soup.find_all("td")[76].get_text()

			availability = soup.find_all("td")[78].get_text()

			net_debt = soup.find_all("td")[80].get_text()

			current_assets = soup.find_all("td")[82].get_text()

			net_worth = soup.find_all("td")[84].get_text()

			net_revenue_3m = soup.find_all("td")[86].get_text()

			net_revenue_12m = soup.find_all("td")[88].get_text()

			EBIT_3m = soup.find_all("td")[90].get_text()

			EBIT_12m = soup.find_all("td")[92].get_text()

			net_profit_3m = soup.find_all("td")[94].get_text()

			net_profit_12m = soup.find_all("td")[96].get_text()

			print("""
====================================================================
|                       STOCK MARKET FINDER                        |
====================================================================
|                           VISÃO GERAL                            |
====================================================================
>PAPEL: {0}                               
-------------------------------------------------------------------|
>COTAÇÃO: {1}
-------------------------------------------------------------------|
>TIPO: {2}                                
-------------------------------------------------------------------|
>DATA DA ÚLTIMA COTAÇÃO: {3}
-------------------------------------------------------------------|
>EMPRESA: {4}                             
-------------------------------------------------------------------|
>MÍN DAS ÚLTIMAS 52 SEMANAS: {5}
-------------------------------------------------------------------|
>SETOR: {6}                               
-------------------------------------------------------------------|
>MÁX DAS ÚLTIMAS 52 SEMANAS: {7}
-------------------------------------------------------------------|
>SUBSETOR: {8}                            
-------------------------------------------------------------------|
>VOLUME MÉDIO ($) DOS ÚLTIMOS 2 MESES: {9}
-------------------------------------------------------------------|
>VALOR DE MERCADO: {10}
-------------------------------------------------------------------|                   
>DATA DO ÚLTIMO BALANÇO: {11} 
-------------------------------------------------------------------|
>VALOR DE FIRMA: {12}                     
-------------------------------------------------------------------|
>NÚMERO DE AÇÕES: {13}
====================================================================
|                           OSCILAÇÕES                             |
====================================================================
>DIA: ###                                 
-------------------------------------------------------------------|
>MÊS: ###                                 
-------------------------------------------------------------------|
>30 DIAS: ###                             
-------------------------------------------------------------------|
>12 MESES: ###                            
-------------------------------------------------------------------|
>2018: ###                               
-------------------------------------------------------------------|
>2017: ###                                
-------------------------------------------------------------------|
>2016: ###                                
-------------------------------------------------------------------|
>2015: ###                                
-------------------------------------------------------------------|
>2014: ###                                
-------------------------------------------------------------------|
>2013: ###                               
====================================================================
|                           INDICADORES                            |
====================================================================
>DPA: {14}        
-------------------------------------------------------------------|            
>DIV.YIELD: {15}
-------------------------------------------------------------------|
>P/L: {16}
-------------------------------------------------------------------|
>LPA: {17}
-------------------------------------------------------------------|
>P/VP: {18}                 
-------------------------------------------------------------------|
>VPA: {19}
-------------------------------------------------------------------|
>P/EBIT: {20}                    
-------------------------------------------------------------------|
>MARG.BRUTA: {21}
-------------------------------------------------------------------|
>PSR: {22}               
-------------------------------------------------------------------|
>MARG.EBIT: {23}
-------------------------------------------------------------------|
>P/ATIVOS: {24}             
-------------------------------------------------------------------|
>MARG.LÍQ: {25}
-------------------------------------------------------------------|
>P/CAP.GIRO: {26}
-------------------------------------------------------------------|
>EBIT/ATIVO: {27}
-------------------------------------------------------------------|
>P/ATIVO.CIRC: {28}              
-------------------------------------------------------------------|
>ROIC: {29}
-------------------------------------------------------------------|
>ROE: {30}                
-------------------------------------------------------------------|
>VF/EBIT: {31}
-------------------------------------------------------------------|
>LÍQ.CORRENTE: {32}            
-------------------------------------------------------------------|
>GIRO ATIVOS: {33}
====================================================================
|                 BALANÇO PATRIMONIAL                              |
====================================================================
>DÍVIDA BRUTA / PATRIMÔNIO: {34}         
-------------------------------------------------------------------|              
>ATIVO: {35}          
-------------------------------------------------------------------|
>DÍVIDA BRUTA: {36}              
-------------------------------------------------------------------|
>DISPONIBILIDADES: {37}                   
-------------------------------------------------------------------|
>DÍVIDA LÍQUIDA: {38}
-------------------------------------------------------------------|
>ATIVO CIRCULANTE: {39}                   
-------------------------------------------------------------------|
>PATRIMÔNIO LÍQUIDO: {40}
====================================================================
|                DADOS DEMONSTRATIVOS DE RESULTADOS                |
====================================================================
|                         ÚLTIMOS 3 MESES                          |
====================================================================
>RECEITA LÍQUIDA: {41}
-------------------------------------------------------------------|
>EBIT: {43}
-------------------------------------------------------------------|
>LUCRO LÍQUIDO: {45}
====================================================================
|                         ÚLTIMOS 12 MESES                         |
====================================================================
>RECEITA LÍQUIDA: {42}
-------------------------------------------------------------------|
>EBIT: {44} 
-------------------------------------------------------------------|
>LUCRO LÍQUIDO: {46}
====================================================================

""".format(ticker, quotation, kind, date_last_neg, company, min_52, sector, max_52, sub_sector, average_vol, market_value,
	last_balance_sheet, enterprise_value, stock_number, dividend_per_stock, dividend_yield, price_profit, proftit_per_stock, equity_value,
	equity_value_per_stock, price_per_EBIT, gross_margin, price_sales_ratio, margin_EBIT, price_asset, net_margin, price_working_capital,
	EBIT_asset, price_liq_current_asset, return_on_invested_capital, return_on_equity, enterprise_value_EBIT, liquid_current, spin_asset,
	gross_debt_patrimony, own_assets, gross_debt, availability, net_debt, current_assets, net_worth, net_revenue_3m, net_revenue_12m, 
	EBIT_3m, EBIT_12m, net_profit_3m, net_profit_12m))

			break

		elif Option == 2:

			print("\n")

			answer = str(input("SMF_BOT --> Qual o Ativo desejado? (Digite o código do Ativo) \nResposta -> "))

			url = 'https://www.comparandus.com.br/acao/%s' % (answer.upper())

			page = urllib.request.urlopen(url)

			soup = BeautifulSoup(page, 'html5lib')

			os.system("cls" or "clear")

			ticker = soup.find_all("td")[1].get_text()

			quotation = soup.find_all("td")[3].get_text()

			kind = soup.find_all("td")[5].get_text()

			date_last_neg = soup.find_all("td")[7].get_text()

			company = soup.find_all("td")[9].get_text()

			min_52 = soup.find_all("td")[11].get_text()

			sector = soup.find_all("td")[13].get_text()

			max_52 = soup.find_all("td")[15].get_text()

			sub_sector = soup.find_all("td")[17].get_text()

			average_vol = soup.find_all("td")[19].get_text()

			market_value = soup.find_all("td")[21].get_text()

			last_balance_sheet = soup.find_all("td")[23].get_text()

			enterprise_value = soup.find_all("td")[25].get_text()

			stock_number = soup.find_all("td")[27].get_text()

			print("""
====================================================================
|                       STOCK MARKET FINDER                        |
====================================================================
|                           VISÃO GERAL                            |
====================================================================
>PAPEL: {0}                               
-------------------------------------------------------------------|
>COTAÇÃO: {1}
-------------------------------------------------------------------|
>TIPO: {2}                                
-------------------------------------------------------------------|
>DATA DA ÚLTIMA COTAÇÃO: {3}
-------------------------------------------------------------------|
>EMPRESA: {4}                             
-------------------------------------------------------------------|
>MÍN DAS ÚLTIMAS 52 SEMANAS: {5}
-------------------------------------------------------------------|
>SETOR: {6}                               
-------------------------------------------------------------------|
>MÁX DAS ÚLTIMAS 52 SEMANAS: {7}
-------------------------------------------------------------------|
>SUBSETOR: {8}                            
-------------------------------------------------------------------|
>VOLUME MÉDIO ($) DOS ÚLTIMOS 2 MESES: {9}
-------------------------------------------------------------------|
>VALOR DE MERCADO: {10}
-------------------------------------------------------------------|                   
>DATA DO ÚLTIMO BALANÇO: {11} 
-------------------------------------------------------------------|
>VALOR DE FIRMA: {12}                     
-------------------------------------------------------------------|
>NÚMERO DE AÇÕES: {13}
====================================================================

""".format(ticker, quotation, kind, date_last_neg, company, min_52, sector, max_52, sub_sector, average_vol, 
	market_value, last_balance_sheet, enterprise_value, stock_number))

			break

		elif Option == 3:

			print("\n")

			answer = str(input("SMF_BOT --> Qual o Ativo desejado? (Digite o código do Ativo) \nResposta -> "))

			url = 'https://www.comparandus.com.br/acao/%s' % (answer.upper())

			page = urllib.request.urlopen(url)

			soup = BeautifulSoup(page, 'html5lib')

			os.system("cls" or "clear")

			dividend_per_stock = soup.find_all("td")[30].get_text()

			dividend_yield = soup.find_all("td")[32].get_text()

			price_profit = soup.find_all("td")[34].get_text()

			proftit_per_stock = soup.find_all("td")[36].get_text()

			equity_value = soup.find_all("td")[38].get_text()

			equity_value_per_stock = soup.find_all("td")[40].get_text()

			price_per_EBIT = soup.find_all("td")[42].get_text()

			gross_margin = soup.find_all("td")[44].get_text()

			price_sales_ratio = soup.find_all("td")[46].get_text()

			margin_EBIT = soup.find_all("td")[48].get_text()

			price_asset = soup.find_all("td")[50].get_text()

			net_margin = soup.find_all("td")[52].get_text()

			price_working_capital = soup.find_all("td")[54].get_text()

			EBIT_asset = soup.find_all("td")[56].get_text()

			price_liq_current_asset = soup.find_all("td")[58].get_text()

			return_on_invested_capital = soup.find_all("td")[62].get_text()

			return_on_equity = soup.find_all("td")[64].get_text()

			enterprise_value_EBIT = soup.find_all("td")[66].get_text()

			liquid_current = soup.find_all("td")[68].get_text()

			spin_asset = soup.find_all("td")[70].get_text()

			print("""
====================================================================
|                       STOCK MARKET FINDER                        |
====================================================================
|                           INDICADORES                            |
====================================================================
>DPA: {0}        
-------------------------------------------------------------------|            
>DIV.YIELD: {1}
-------------------------------------------------------------------|
>P/L: {2}
-------------------------------------------------------------------|
>LPA: {3}
-------------------------------------------------------------------|
>P/VP: {4}                 
-------------------------------------------------------------------|
>VPA: {5}
-------------------------------------------------------------------|
>P/EBIT: {6}                    
-------------------------------------------------------------------|
>MARG.BRUTA: {7}
-------------------------------------------------------------------|
>PSR: {8}               
-------------------------------------------------------------------|
>MARG.EBIT: {9}
-------------------------------------------------------------------|
>P/ATIVOS: {10}             
-------------------------------------------------------------------|
>MARG.LÍQ: {11}
-------------------------------------------------------------------|
>P/CAP.GIRO: {12}
-------------------------------------------------------------------|
>EBIT/ATIVO: {13}
-------------------------------------------------------------------|
>P/ATIVO.CIRC: {14}              
-------------------------------------------------------------------|
>ROIC: {15}
-------------------------------------------------------------------|
>ROE: {16}                
-------------------------------------------------------------------|
>VF/EBIT: {17}
-------------------------------------------------------------------|
>LÍQ.CORRENTE: {18}            
-------------------------------------------------------------------|
>GIRO ATIVOS: {19}
====================================================================

""".format(dividend_per_stock, dividend_yield, price_profit, proftit_per_stock, equity_value, equity_value_per_stock, price_per_EBIT, 
	gross_margin, price_sales_ratio, margin_EBIT, price_asset, net_margin, price_working_capital, EBIT_asset, price_liq_current_asset,
	return_on_invested_capital, return_on_equity, enterprise_value_EBIT, liquid_current, spin_asset))

			break

		elif Option == 4:

			print("\n")

			answer = str(input("SMF_BOT --> Qual o Ativo desejado? (Digite o código do Ativo) \nResposta -> "))

			url = 'https://www.comparandus.com.br/acao/%s' % (answer.upper())

			page = urllib.request.urlopen(url)

			soup = BeautifulSoup(page, 'html5lib')

			os.system("cls" or "clear")

			gross_debt_patrimony = soup.find_all("td")[72].get_text() 

			own_assets = soup.find_all("td")[74].get_text()

			gross_debt = soup.find_all("td")[76].get_text()

			availability = soup.find_all("td")[78].get_text()

			net_debt = soup.find_all("td")[80].get_text()

			current_assets = soup.find_all("td")[82].get_text()

			net_worth = soup.find_all("td")[84].get_text()

			print("""
====================================================================
|                       STOCK MARKET FINDER                        |
====================================================================
|                       BALANÇO PATRIMONIAL                        |
====================================================================
>DÍVIDA BRUTA / PATRIMÔNIO: {0}         
-------------------------------------------------------------------|              
>ATIVO: {1}          
-------------------------------------------------------------------|
>DÍVIDA BRUTA: {2}              
-------------------------------------------------------------------|
>DISPONIBILIDADES: {3}                   
-------------------------------------------------------------------|
>DÍVIDA LÍQUIDA: {4}
-------------------------------------------------------------------|
>ATIVO CIRCULANTE: {5}                   
-------------------------------------------------------------------|
>PATRIMÔNIO LÍQUIDO: {6}
====================================================================

""".format(gross_debt_patrimony, own_assets, gross_debt, availability, net_debt, current_assets, net_worth))

			break

		elif Option == 5:

			print("\n")

			answer = str(input("SMF_BOT --> Qual o Ativo desejado? (Digite o código do Ativo) \nResposta -> "))

			url = 'https://www.comparandus.com.br/acao/%s' % (answer.upper())

			page = urllib.request.urlopen(url)

			soup = BeautifulSoup(page, 'html5lib')

			os.system("cls" or "clear")

			net_revenue_3m = soup.find_all("td")[86].get_text()

			net_revenue_12m = soup.find_all("td")[88].get_text()

			EBIT_3m = soup.find_all("td")[90].get_text()

			EBIT_12m = soup.find_all("td")[92].get_text()

			net_profit_3m = soup.find_all("td")[94].get_text()

			net_profit_12m = soup.find_all("td")[96].get_text()

			print("""
====================================================================
|                       STOCK MARKET FINDER                        |
====================================================================
|                DADOS DEMONSTRATIVOS DE RESULTADOS                |
====================================================================
|                         ÚLTIMOS 3 MESES                          |
====================================================================
>RECEITA LÍQUIDA: {0}
-------------------------------------------------------------------|
>EBIT: {1}
-------------------------------------------------------------------|
>LUCRO LÍQUIDO: {2}
====================================================================
|                         ÚLTIMOS 12 MESES                         |
====================================================================
>RECEITA LÍQUIDA: {3}
-------------------------------------------------------------------|
>EBIT: {4} 
-------------------------------------------------------------------|
>LUCRO LÍQUIDO: {5}
====================================================================

""".format(net_revenue_3m, net_revenue_12m, EBIT_3m, EBIT_12m, net_profit_3m, net_profit_12m))

			break

		elif Option == 6:

			print("\n")

			answer = str(input("SMF_BOT --> Qual o Ativo desejado? (Digite o código do Ativo) \nResposta -> "))

			url = 'https://www.comparandus.com.br/acao/%s' % (answer.upper())

			page = urllib.request.urlopen(url)

			soup = BeautifulSoup(page, 'html5lib')

			market_value = soup.find_all("td")[21].get_text()

			to_drop_1 = "."
			for i in range(0, len(to_drop_1)):
				market_value = market_value.replace(to_drop_1[i],"")

			if int(market_value) > 500000000:
				discretion_1 = "SIM"

			else:
				discretion_1 = "NÃO"

			kind = soup.find_all("td")[5].get_text()

			if kind == "ON" or kind == "PN":
				discretion_2 = "SIM"

			else:
				discretion_2 = "NÃO"

			liquid_current = soup.find_all("td")[68].get_text()

			to_drop_2 = ","
			for i in range(0, len(to_drop_2)):
				liquid_current = liquid_current.replace(to_drop_2[i],".")

			if float(liquid_current) > 1.5:
				discretion_3 = "SIM"

			else:
				discretion_3 = "NÃO"

			return_on_equity = soup.find_all("td")[64].get_text()

			to_drop_3 = "%,"
			for i in range(0, len(to_drop_3)):
				return_on_equity = return_on_equity.replace(to_drop_3[i],".")

			return_on_equity = return_on_equity[:-1]

			if (float(return_on_equity)/100) > 20/100:
				discretion_4 = "SIM"

			else:
				discretion_4 = "NÃO"

			gross_debt_patrimony = soup.find_all("td")[72].get_text()

			to_drop_4 = "%,"
			for i in range(0, len(to_drop_4)):
				gross_debt_patrimony = gross_debt_patrimony.replace(to_drop_4[i],".")

			gross_debt_patrimony = gross_debt_patrimony[:-1]

			if (float(gross_debt_patrimony)/100) < 50/100:
				discretion_5 = "SIM"

			else:
				discretion_5 = "NÃO"

			net_profit_12m = soup.find_all("td")[96].get_text()

			net_revenue_12m = soup.find_all("td")[88].get_text()

			to_drop_5 = "MB"
			for i in range(0, len(to_drop_5)):
				net_profit_12m = net_profit_12m.replace(to_drop_5[i],"")
				net_revenue_12m = net_revenue_12m.replace(to_drop_5[i],"")

			if (float(net_profit_12m) / float(net_revenue_12m))*100 < 5:
				discretion_6 = "SIM"

			else:
				discretion_6 = "NÃO"

			net_profit_12m = soup.find_all("td")[96].get_text()

			net_profit_3m = soup.find_all("td")[94].get_text()

			to_drop_6 = "MB"
			for i in range(0, len(to_drop_6)):
				net_profit_12m = net_profit_12m.replace(to_drop_6[i],"")
				net_profit_3m = net_profit_3m.replace(to_drop_6[i],"")

			if float(net_profit_12m) - (float(net_profit_3m)*4) > 0:
				discretion_7 = "SIM"

			else:
				discretion_7 = "NÃO"

			dividend_yield = soup.find_all("td")[32].get_text()

			to_drop_7 = ",%"
			for i in range(0, len(to_drop_7)):
				dividend_yield = dividend_yield.replace(to_drop_7[i],".")

			dividend_yield = dividend_yield[:-1]

			if (float(dividend_yield)/100) > 0:
				discretion_8 = "SIM"

			else:
				discretion_8 = "NÃO"

			equity_value = soup.find_all("td")[38].get_text()

			to_drop_8 = ","
			for i in range(0, len(to_drop_8)):
				equity_value = equity_value.replace(to_drop_8[i],".")

			if float(equity_value) < 1:
				discretion_9 = "SIM"

			else:
				discretion_9 = "NÃO"

			price_profit = soup.find_all("td")[34].get_text()

			to_drop_9 = ","
			for i in range(0, len(to_drop_9)):
				price_profit = price_profit.replace(to_drop_9[i],".")

			if float(price_profit) < 15:
				discretion_10 = "SIM"

			else:
				discretion_10 = "NÃO"

			average_vol = soup.find_all("td")[19].get_text()

			to_drop_10 = "."
			for i in range(0, len(to_drop_10)):
				average_vol = average_vol.replace(to_drop_10[i],"")

			if int(average_vol) > 3000000:
				discretion_11 = "SIM"

			else:
				discretion_11 = "NÃO"

			print("""
+~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
|                                          CHECKLIST DO ATIVO/EMPRESA!                                        |
+~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
|>(1) O VALOR DE MERCADO é maior que R$ 500 milhões? - [{}]                                                  |
|                                                                                                             |
|COMPANHIAS COM PEQUENO VALOR DE MERCADO PODEM ESTAR SUJEITAS A ADVERSIDADES ACIMA DO NORMAL, QUANTO A        |
|QUESTÕES FINANCEIRAS, ECONÔMICAS, POLÍTICAS E SOCIAIS. POR OUTRO LADO, EMPRESAS DE GRANDE VALOR DE MERCADO   |
|PODEM APRESENTAR MAIOR CAPACIDADE DE SUPERAÇÃO EM MOMENTOS DE ADVERSIDADE.                                   |
|=============================================================================================================|
|>(2) Possui algum nível de GOVERNANÇA CORPORATIVA? - [{}]                                                   |
|                                                                                                             |
|AS BOAS PRÁTICAS DE GOVERNANÇA CORPORATIVA TÊM A FINALIDADE DE AUMENTAR A TRANSPARÊNCIA E A QUALIDADE NA     |
|DIVULGAÇÃO DE INFORMAÇÕES AOS ACIONISTAS. O MERCADO AVALIA QUE OS INVESTIDORES ESTARÃO DISPOSTOS A PAGAR     |
|MAIS PELAS AÇÕES DE EMPRESAS QUE DEMONSTREM RESPEITO AOS DIREITOS DOS ACIONISTAS E QUE ADOTEM BOAS PRÁTICAS  |
|DE GOVERNANÇA.                                                                                               |
|=============================================================================================================|
|>(3) A LIQUIDEZ CORRENTE é maior que 1,5x? - [{}]                                                           |
|                                                                                                             |
|ATIVO CIRCULANTE DIVIDIDO PELO PASSIVO CIRCULANTE. ESTE ÍNDICE INDICA QUANTO A EMPRESA TEM A RECEBER NO      |
|CURTO PRAZO EM RELAÇÃO A CADA UNIDADE MONETÁRIA QUE DEVE NO MESMO PERÍODO. QUANTO MAIOR A LIQUIDEZ CORRENTE, |
|MAIS ALTA SE APRESENTA A CAPACIDADE DA EMPRESA EM FINANCIAR SUAS NECESSIDADES DE CAPITAL DE GIRO.            |
|=============================================================================================================|
|>(4) O RETORNO SOBRE PATRIMÔNIO LÍQUIDO (ROE) é maior que 20%? - [{}]                                       |
|                                                                                                             |
|RELAÇÃO ENTRE O LUCRO LÍQUIDO DOS ÚLTIMOS 12 MESES E O PATRIMÔNIO LÍQUIDO. ELE MOSTRA A RENTABILIDADE QUE A  | 
|EMPRESA ESTÁ GERANDO SOBRE O SEU PRÓPRIO PATRIMÔNIO. EM OUTRAS PALAVRAS, SOBRE O CAPITAL PRÓPRIO.            |
|=============================================================================================================|
|>(5) A relação DÍVIDA BRUTA / PATRIMÔNIO LÍQUIDO é menor que 50%? - [{}]                                    |
|                                                                                                             |
|DÍVIDA BRUTA TOTAL (SOMA DE EMPRÉSTIMOS, FINANCIAMENTOS E DEBÊNTURES DE CURTO E LONGO PRAZO) DIVIDIDO PELO   | 
|PATRIMÔNIO LÍQUIDO. QUANTO MAIOR, MAIS RISCO A EMPRESA ESTÁ CORRENDO.                                        |
|=============================================================================================================|
|>(6) Possui CRESCIMENTO DOS LUCROS acima de 5% A.A? - [{}]                                                  |
|                                                                                                             |
|A CAPACIDADE DA COMPANHIA APRESENTAR CRESCIMENTO DOS LUCROS DEMONSTRA QUE A ADMINISTRAÇÃO E A ESTRATÉGIA DE  | 
|MERCADO ESTÃO, AMBAS, CONVERGINDO PARA O SUCESSO DO EMPREENDIMENTO, O QUE FICA EVIDENCIADO NA TAXA ASCENDENTE| 
|DOS LUCROS DIVULGADOS.                                                                                       |
|=============================================================================================================|
|>(7) POSSUI LUCROS CONSTANTES nos últimos 5 anos? - [{}]                                                    |
|                                                                                                             |
|A CAPACIDADE DA COMPANHIA APRESENTAR ESTABILIDADE DE LUCROS OU PELO MENOS ALGUM LUCRO EM DETERMINADO PERÍODO,| 
|DEMONSTRA QUE O INTERESSE DA GESTÃO ESTÁ CONVERGINDO PARA O EVOLUÇÃO DO EMPREENDIMENTO, DADAS AS CONDIÇÕES   |
|MICRO E MACROECONÔMICAS DO PERÍODO, O QUE FICA EVIDENCIADO NA ESTABILIDADE DOS LUCROS DIVULGADOS.            |
|=============================================================================================================|
|>(8) Distribuiu DIVIDENDOS nos últimos 5 anos? - [{}]                                                       |
|                                                                                                             |
|PAGAMENTOS ININTERRUPTOS DE DIVIDENDOS, AO LONGO DE DETERMINADO PERÍODO, DEMONSTRA, NESTE QUESITO, QUE OS    |
|INTERESSES DOS ACIONISTAS ESTÃO SENDO ATENDIDOS DE ACORDO COM A LEGISLAÇÃO VIGENTE. CABE LEMBRAR QUE EMPRESAS|
|QUE APRESENTAM REGULARIDADE DE PAGAMENTO DE DIVIDENDOS SÃO MAIS PROCURADAS PELOS INVESTIDORES.               |
|=============================================================================================================|
|>(9) A relação PREÇO / VALOR PATRIMONIAL (P/VPA) é menos que 2x? - [{}]                                     |
|                                                                                                             |
|COMPARA O VALOR DE MERCADO DA EMPRESA COM SEU VALOR CONTÁBIL. EM TESE, QUANTO MAIS BAIXO ESTE ÍNDICE, MAIS   | 
|BARATA É A EMPRESA.                                                                                          |
|=============================================================================================================|
|>(10) A relação PREÇO / LUCRO (P/L) é menor que 15x? - [{}]                                                 |
|                                                                                                             |
|RELAÇÃO ENTRE O VALOR DE MERCADO DA EMPRESA DIVIDIDO PELO LUCRO DOS ÚLTIMOS 12 MESES. O ÍNDICE P/L INDICA O  |
|NÚMERO DE ANOS QUE UM INVESTIDOR LEVARIA PARA RECUPERAR O CAPITAL INVESTIDO. EM TESE, QUANTO MENOR ESTA      |
|RELAÇÃO, MAIS BARATA ESTÁ A EMPRESA.                                                                         |
|=============================================================================================================|
|>(11) O VOLUME MÉDIO DIÁRIO (21d) é maior que R$ 1 milhão? - [{}]                                           |
|                                                                                                             |
|REPRESENTA O VOLUME MÉDIO NEGOCIADO NOS ÚLTIMOS 21 PREGÕES. QUANDO MAIOR ESTE VOLUME, MAIOR A LIQUIDEZ DA    |
|AÇÃO, O QUE EQUIVALE A DIZER QUE ESSA AÇÃO É MAIS NEGOCIADA QUE OUTRA COM VOLUME MÉDIO INFERIOR. QUANTO MAIOR|
|A LIQUIDEZ, MELHOR PARA O INVESTIDOR.                                                                        |
+~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
|                                          CHECKLIST DO ATIVO/EMPRESA!                                        |
+~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+

""".format(discretion_1, discretion_2, discretion_3, discretion_4, discretion_5, discretion_6, discretion_7, 
	discretion_8, discretion_9, discretion_10, discretion_11))
		
			break

		elif Option == 7:

			print("\n")
			
			answer = str(input("SMF_BOT --> Qual o Ativo desejado? (Digite o código do Ativo) \nResposta -> "))

			url = 'https://www.comparandus.com.br/acao/%s' % (answer.upper())

			page = urllib.request.urlopen(url)

			soup = BeautifulSoup(page, 'html5lib')

			market_value = soup.find_all("td")[21].get_text()

			to_drop_1 = "."
			for i in range(0, len(to_drop_1)):
				market_value = market_value.replace(to_drop_1[i],"")

			if int(market_value) > 500000000:
				discretion_1 = "SIM"

			else:
				discretion_1 = "NÃO"

			kind = soup.find_all("td")[5].get_text()

			if kind == "ON" or kind == "PN":
				discretion_2 = "SIM"

			else:
				discretion_2 = "NÃO"

			liquid_current = soup.find_all("td")[68].get_text()

			to_drop_2 = ","
			for i in range(0, len(to_drop_2)):
				liquid_current = liquid_current.replace(to_drop_2[i],".")

			if float(liquid_current) > 1.5:
				discretion_3 = "SIM"

			else:
				discretion_3 = "NÃO"

			return_on_equity = soup.find_all("td")[64].get_text()

			to_drop_3 = "%,"
			for i in range(0, len(to_drop_3)):
				return_on_equity = return_on_equity.replace(to_drop_3[i],".")

			return_on_equity = return_on_equity[:-1]

			if (float(return_on_equity)/100) > 20/100:
				discretion_4 = "SIM"

			else:
				discretion_4 = "NÃO"

			gross_debt_patrimony = soup.find_all("td")[72].get_text()

			to_drop_4 = "%,"
			for i in range(0, len(to_drop_4)):
				gross_debt_patrimony = gross_debt_patrimony.replace(to_drop_4[i],".")

			gross_debt_patrimony = gross_debt_patrimony[:-1]

			if (float(gross_debt_patrimony)/100) < 50/100:
				discretion_5 = "SIM"

			else:
				discretion_5 = "NÃO"

			net_profit_12m = soup.find_all("td")[96].get_text()

			net_revenue_12m = soup.find_all("td")[88].get_text()

			to_drop_5 = "MB"
			for i in range(0, len(to_drop_5)):
				net_profit_12m = net_profit_12m.replace(to_drop_5[i],"")
				net_revenue_12m = net_revenue_12m.replace(to_drop_5[i],"")

			if (float(net_profit_12m) / float(net_revenue_12m))*100 < 5:
				discretion_6 = "SIM"

			else:
				discretion_6 = "NÃO"

			net_profit_12m = soup.find_all("td")[96].get_text()

			net_profit_3m = soup.find_all("td")[94].get_text()

			to_drop_6 = "MB"
			for i in range(0, len(to_drop_6)):
				net_profit_12m = net_profit_12m.replace(to_drop_6[i],"")
				net_profit_3m = net_profit_3m.replace(to_drop_6[i],"")

			if float(net_profit_12m) - (float(net_profit_3m)*4) > 0:
				discretion_7 = "SIM"

			else:
				discretion_7 = "NÃO"

			dividend_yield = soup.find_all("td")[32].get_text()

			to_drop_7 = ",%"
			for i in range(0, len(to_drop_7)):
				dividend_yield = dividend_yield.replace(to_drop_7[i],".")

			dividend_yield = dividend_yield[:-1]

			if (float(dividend_yield)/100) > 0:
				discretion_8 = "SIM"

			else:
				discretion_8 = "NÃO"

			equity_value = soup.find_all("td")[38].get_text()

			to_drop_8 = ","
			for i in range(0, len(to_drop_8)):
				equity_value = equity_value.replace(to_drop_8[i],".")

			if float(equity_value) < 1:
				discretion_9 = "SIM"

			else:
				discretion_9 = "NÃO"

			price_profit = soup.find_all("td")[34].get_text()

			to_drop_9 = ","
			for i in range(0, len(to_drop_9)):
				price_profit = price_profit.replace(to_drop_9[i],".")

			if float(price_profit) < 15:
				discretion_10 = "SIM"

			else:
				discretion_10 = "NÃO"

			average_vol = soup.find_all("td")[19].get_text()

			to_drop_10 = "."
			for i in range(0, len(to_drop_10)):
				average_vol = average_vol.replace(to_drop_10[i],"")

			if int(average_vol) > 3000000:
				discretion_11 = "SIM"

			else:
				discretion_11 = "NÃO"

			list_checklist_asset = [discretion_1, discretion_2, discretion_3, discretion_4, discretion_5, discretion_6, discretion_7, discretion_8, 
			discretion_9, discretion_10, discretion_11]

			count_yes = list_checklist_asset.count('SIM')
			count_no = list_checklist_asset.count('NÃO')

			if count_yes <= 4:
				asset_recommendation = "VENDER"

			elif count_yes > 4 and count_yes <= 8:
				asset_recommendation = "MANTER"

			elif count_yes > 8: 
				asset_recommendation = "COMPRAR"

			score_asset = round((count_yes / 11) * 10, 2)

			print("""
+~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
|                                            RECOMENDAÇÕES DO ATIVO!                                          |
+~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
|>RESUMO:                                                                                                     |
|O ATIVO OBTEVE UM SCORE IGUAL A [{0}], LOGO SUA PONTUAÇÃO MÉDIA DE ACERTO FOI IGUAL A [{1}].                  |
|RECOMENDAMOS QUE AVALIE [{2}] O ATIVO.                                                                   |
|=============================================================================================================|
|>LEITURA DOS DADOS ANALISADOS:                                                                               |
|>(1):                                                                                                        |
|SE A PONTUAÇÃO MÉDIA FOR MENOR OU IGUAL A 4, RECOMENDAMOS VENDER O ATIVO, SE EXISTIR POSIÇÃO, CASO NÃO       |
|EXISTA, NÃO RECOMENDAMOS COMPRAR.                                                                            |
|-------------------------------------------------------------------------------------------------------------|
|>(2):                                                                                                        |
|SE A PONTUAÇÃO MÉDIA FOR MAIOR QUE 4 E MENOR OU IGUAL A 8, RECOMENDAMOS MANTER O ATIVO, SE EXISTIR POSIÇÃO,  |
|CASO NÃO EXISTA, NÃO RECOMENDAMOS COMPRAR.                                                                   |
|-------------------------------------------------------------------------------------------------------------|
|>(3):                                                                                                        |
|SE A PONTUAÇÃO MÉDIA FOR MAIOR QUE 8, RECOMENDAMOS COMPRAR O ATIVO, SE EXISTIR POSIÇÃO NÃO REALIZE A VENDA,  |
|CASO NÃO EXISTA, RECOMENDAMOS A CONSIDERAÇÃO DE COMPRA.                                                      |
|=============================================================================================================|
|>(1)OBS:                                                                                                     |
|AS RECOMENDAÇÕES SÃO FEITAS ATRAVÉS DE CRITÉRIOS GERAIS, PORÉM CADA INVESTIDOR DEVE POSSUIR UMA              |
|ESTRATÉGIA PRÓPRIA, VISANDO A MELHOR FORMA DE OBTENÇÃO DE PATRIMÔNIO, NO LONGO PRAZO, OU OBTENÇÃO DE LUCRO,  |
|NO CURTO PRAZO. POR ISSO, É SIGNIFICATIVO QUE A ESTRATÉGIA SEJA ELABORADA VISANDO A OBTENÇÃO DAS METAS,      |
|OBJETIVOS E RESULTADOS PRETENDIDOS PELO INVESTIDOR.                                                          |
|-------------------------------------------------------------------------------------------------------------|
|>(2)OBS:                                                                                                     |
|A ANÁLISE DE RECOMENDAÇÃO PROCURA OFERECER UMA VISÃO GERAL SOBRE A SITUAÇÃO DA EMPRESA DE ACORDO COM         |
|CRITÉRIOS FUNDAMENTALISTAS. A PONTUAÇÃO BUSCA APRESENTAR AO INVESTIDOR CRITÉRIOS VALIOSOS QUE VALEM A PENA   |
|SEREM CONSIDERADOS NA HORA DA AQUISIÇÃO DA AÇÃO ANALISADA. RESSALTAMOS AINDA QUE RENTABILIDADE PASSADA NÃO É |
|GARANTIA DE RENTABILIDADE FUTURA.                                                                            |
|-------------------------------------------------------------------------------------------------------------|
|>(3)OBS:                                                                                                     |
|RECOMENDAMOS AINDA QUE ANTES DE QUALQUER TOMADA DE DECISÃO O INVESTIDOR REALIZE IMPRETERIVELMENTE            |
|TODAS AS ANÁLISES E CÁLCULOS DE FORMA MANUAL, AFIM DE QUE POSSA CONFERERIR OS DADOS APRESENTADOS PELO        |
|SOFTWARE.                                                                                                    |
|-------------------------------------------------------------------------------------------------------------|
|>(4)OBS:                                                                                                     |
|NÃO NOS RESPONSABILIZAMOS POR NENHUMA TOMADA DE DECISÃO PROVINDA DE QUALQUER TIPO OU FORMA DE                |
|RECOMENDAÇÃO DESTE SOFTWARE, A AQUISIÇÃO DE QUALQUER ATIVO, É DE INTERINA RESPONSABILIDADE APENAS, E SOMENTE |
|APENAS, DO INVESTIDOR.                                                                                       |
+~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
|                                            RECOMENDAÇÕES DO ATIVO!                                          |
+~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+

""".format(score_asset, count_yes, asset_recommendation))
		
			break

		elif Option == 8:
			Banners_SMF.Banners_Prints_1()

			break

		elif Option == 9:
			Banners_SMF.Banners_Prints_2()

			break

	while Option not in range(1,10):
		print("\n[!] Insira um valor contido na opção do menu.")
		break

except KeyboardInterrupt:
	print('\n[!] Saindo...')
except ValueError:
	print('\n[!] Insira um valor correto.')