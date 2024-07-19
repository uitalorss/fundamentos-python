#! /usr/bin/env python3

import logging

#Criação da instância
log = logging.Logger("logs", logging.DEBUG)

#Level
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

#Formatação
fmt = logging.Formatter("%(asctime)s    %(name)s    %(levelname)s    l:%(lineno)d    f:%(filename)s    %(message)s")
ch.setFormatter(fmt)

#Destino
log.addHandler(ch)


log.debug("Mensagem pro dev, QA, sysadmin")
log.info("Mensagem geral para os usuários")
log.warning("Aviso que não causa erro.")
log.error("Erro que afeta uma única execução")
log.critical("Erro que afeta todo o sistema. Ex: O banco de dados sumiu")