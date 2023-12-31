
class HistoryLeadsEntity():
     
    @property
    def id(self):
        return self.__id
    
    @property
    def primeiro_nome(self):
        return self.__primeiro_nome

    @property
    def nome(self):
        return self.__nome

    @property
    def email(self):
        return self.__email

    @property
    def empresa(self):
        return self.__empresa

    @property
    def cargo(self):
        return self.__cargo

    @property
    def telefones(self):
        return self.__telefones
    @property
    def site(self):
        return self.__site

    @property
    def criado_em(self):
        return self.__criado_em

    @property
    def estado(self):
        return self.__estado

    @property
    def cidade(self):
        return self.__cidade

    @property
    def twitter(self):
        return self.__twitter

    @property
    def facebook(self):
        return self.__facebook


    @property
    def linkedin(self):
        return self.__linkedin

    @property
    def cadencia(self):
        return self.__cadencia

    @property
    def tipo(self):
        return self.__tipo
        
    @property
    def status(self):
        return self.__status

    @property
    def motivo_perda(self):
        return self.__motivo_perda

    @property
    def vendedor(self):
        return self.__vendedor

    @property
    def recebido_pelo_vendedor_em(self):
        return self.__recebido_pelo_vendedor_em

    @property
    def tempo_resposta_min(self):
        return self.__tempo_resposta_min

    @property
    def iniciado_em(self):
        return self.__iniciado_em

    @property
    def primeira_atividade(self):
        return self.__primeira_atividade

    @property
    def atividades(self):
        return self.__atividades

    @property
    def ultima_atividade(self):
        return self.__ultima_atividade

    @property
    def dias_em_prospeccao(self):
        return self.__dias_em_prospeccao

    @property
    def finalizado_em(self):
        return self.__finalizado_em

    @property
    def origem_campanha(self):
        return self.__origem_campanha

    @property
    def origem_fonte(self):
        return self.__origem_fonte

    @property
    def origem_canal(self):
        return self.__origem_canal

    @property
    def origem_conversao(self):
        return self.__origem_conversao

    @property
    def pesquisas(self):
        return self.__pesquisas

    @property
    def social_points(self):
        return self.__social_points

    @property
    def emails(self):
        return self.__emails

    @property
    def ligacoes(self):
        return self.__ligacoes

    @property
    def atividades_ignoradas(self):
        return self.__atividades_ignoradas
        
    @property
    def pesquisas_ignoradas(self):
        return self.__pesquisas_ignoradas

    @property
    def social_points_ignoradas(self):
        return self.__social_points_ignoradas

    @property
    def emails_ignorados(self):
        return self.__emails_ignorados

    @property
    def ligacoes_ignoradas(self):
        return self.__ligacoes_ignoradas

    @property
    def cnpj(self):
        return self.__cnpj

    @property
    def ramo_empresa(self):

        return self.__ramo_empresa
    @property
    def bu_do_cliente(self):

        return self.__bu_do_cliente
    @property
    def faturamento_dolares(self):

        return self.__faturamento_dolares
    @property
    def faturamento(self):
        return self.__faturamento

    @property
    def qtd_funcionarios(self):
        return self.__qtd_funcionarios

    @property
    def cliente_gavb(self):
        return self.__cliente_gavb

    @property
    def setor_que_atendemos(self):
        return self.__setor_que_atendemos

    @id.setter
    def id(self, value):
        self.__id = value

    @primeiro_nome.setter
    def primeiro_nome(self, value):
        self.__primeiro_nome = value

    @nome.setter
    def nome(self, value):
        self.__nome = value

    @email.setter
    def email(self, value):
        self.__email = value

    @empresa.setter
    def empresa(self, value):
        self.__empresa = value

    @cargo.setter
    def cargo(self, value):
        self.__cargo = value

    @telefones.setter
    def telefones(self, value):
        self.__telefones = value

    @site.setter
    def site(self, value):
        self.__site = value

    @criado_em.setter
    def criado_em(self, value):
        self.__criado_em = value

    @estado.setter
    def estado(self, value):
        self.__estado = value

    @cidade.setter
    def cidade(self, value):
        self.__cidade = value

    @twitter.setter
    def twitter(self, value):
        self.__twitter = value

    @facebook.setter
    def facebook(self, value):
        self.__facebook = value

    @linkedin.setter
    def linkedin(self, value):
        self.__linkedin = value

    @cadencia.setter
    def cadencia(self, value):
        self.__cadencia = value

    @tipo.setter
    def tipo(self, value):
        self.__tipo = value

    @status.setter
    def status(self, value):
        self.__status = value

    @motivo_perda.setter
    def motivo_perda(self, value):
        self.__motivo_perda = value

    @vendedor.setter
    def vendedor(self, value):
        self.__vendedor = value

    @recebido_pelo_vendedor_em.setter
    def recebido_pelo_vendedor_em(self, value):
        self.__recebido_pelo_vendedor_em = value

    @tempo_resposta_min.setter
    def tempo_resposta_min(self, value):
        self.__tempo_resposta_min = value

    @iniciado_em.setter
    def iniciado_em(self, value):
        self.__iniciado_em = value

    @primeira_atividade.setter
    def primeira_atividade(self, value):
        self.__primeira_atividade = value

    @atividades.setter
    def atividades(self, value):
        self.__atividades = value

    @ultima_atividade.setter
    def ultima_atividade(self, value):
        self.__ultima_atividade = value

    @dias_em_prospeccao.setter
    def dias_em_prospeccao(self, value):
        self.__dias_em_prospeccao = value

    @finalizado_em.setter
    def finalizado_em(self, value):
        self.__finalizado_em = value

    @origem_campanha.setter
    def origem_campanha(self, value):
        self.__origem_campanha = value

    @origem_fonte.setter
    def origem_fonte(self, value):
        self.__origem_fonte = value

    @origem_canal.setter
    def origem_canal(self, value):
        self.__origem_canal = value

    @origem_conversao.setter
    def origem_conversao(self, value):
        self.__origem_conversao = value

    @pesquisas.setter
    def pesquisas(self, value):
        self.__pesquisas = value

    @social_points.setter
    def social_points(self, value):
        self.__social_points = value

    @emails.setter
    def emails(self, value):
        self.__emails = value

    @ligacoes.setter
    def ligacoes(self, value):
        self.__ligacoes = value

    @atividades_ignoradas.setter
    def atividades_ignoradas(self, value):
        self.__atividades_ignoradas = value

    @pesquisas_ignoradas.setter
    def pesquisas_ignoradas(self, value):
        self.__pesquisas_ignoradas = value

    @social_points_ignoradas.setter
    def social_points_ignoradas(self, value):
        self.__social_points_ignoradas = value

    @emails_ignorados.setter
    def emails_ignorados(self, value):
        self.__emails_ignorados = value

    @ligacoes_ignoradas.setter
    def ligacoes_ignoradas(self, value):
        self.__ligacoes_ignoradas = value

    @cnpj.setter
    def cnpj(self, value):
        self.__cnpj = value

    @ramo_empresa.setter
    def ramo_empresa(self, value):
        self.__ramo_empresa = value

    @bu_do_cliente.setter
    def bu_do_cliente(self, value):
        self.__bu_do_cliente = value

    @faturamento_dolares.setter
    def faturamento_dolares(self, value):
        self.__faturamento_dolares = value

    @faturamento.setter
    def faturamento(self, value):
        self.__faturamento = value

    @qtd_funcionarios.setter
    def qtd_funcionarios(self, value):
        self.__qtd_funcionarios = value

    @cliente_gavb.setter
    def cliente_gavb(self, value):
        self.__cliente_gavb = value

    @setor_que_atendemos.setter
    def setor_que_atendemos(self, value):
        self.__setor_que_atendemos = value

    def __init__(self):
        self.id = None
        self.primeiro_nome = None
        self.nome = None
        self.email = None
        self.empresa = None
        self.cargo = None
        self.telefones = None
        self.site = None
        self.criado_em = None
        self.estado = None
        self.cidade = None
        self.twitter = None
        self.facebook = None
        self.linkedin = None
        self.cadencia = None
        self.tipo = None
        self.status = None
        self.motivo_perda = None
        self.vendedor = None
        self.recebido_pelo_vendedor_em = None
        self.tempo_resposta_min = None
        self.iniciado_em = None
        self.primeira_atividade = None
        self.atividades = None
        self.ultima_atividade = None
        self.dias_em_prospeccao = None
        self.finalizado_em = None
        self.origem_campanha = None
        self.origem_fonte = None
        self.origem_canal = None
        self.origem_conversao = None
        self.pesquisas = None
        self.social_points = None
        self.emails = None
        self.ligacoes = None
        self.atividades_ignoradas = None
        self.pesquisas_ignoradas = None
        self.social_points_ignoradas = None
        self.emails_ignorados = None
        self.ligacoes_ignoradas = None
        self.cnpj = None
        self.ramo_empresa = None
        self.bu_do_cliente = None
        self.faturamento_dolares = None
        self.faturamento = None
        self.qtd_funcionarios = None
        self.cliente_gavb = None
        self.setor_que_atendemos = None

    def to_dict(self):
        return {
            'id': self.id,
            'primeiro_nome': self.primeiro_nome,
            'nome': self.nome,
            'email': self.email,
            'empresa': self.empresa,
            'cargo': self.cargo,
            'telefones': self.telefones,
            'site': self.site,
            'criado_em': self.criado_em,
            'estado': self.estado,
            'cidade': self.cidade,
            'twitter': self.twitter,
            'facebook': self.facebook,
            'linkedin': self.linkedin,
            'cadencia': self.cadencia,
            'tipo': self.tipo,
            'status': self.status,
            'motivo_perda': self.motivo_perda,
            'vendedor': self.vendedor,
            'recebido_pelo_vendedor_em': self.recebido_pelo_vendedor_em,
            'tempo_resposta_min': self.tempo_resposta_min,
            'iniciado_em': self.iniciado_em,
            'primeira_atividade': self.primeira_atividade,
            'atividades': self.atividades,
            'ultima_atividade': self.ultima_atividade,
            'dias_em_prospeccao': self.dias_em_prospeccao,
            'finalizado_em': self.finalizado_em,
            'origem_campanha': self.origem_campanha,
            'origem_fonte': self.origem_fonte,
            'origem_canal': self.origem_canal,
            'origem_conversao': self.origem_conversao,
            'pesquisas': self.pesquisas,
            'social_points': self.social_points,
            'emails': self.emails,
            'ligacoes': self.ligacoes,
            'atividades_ignoradas': self.atividades_ignoradas,
            'pesquisas_ignoradas': self.pesquisas_ignoradas,
            'social_points_ignoradas': self.social_points_ignoradas,
            'emails_ignorados': self.emails_ignorados,
            'ligacoes_ignoradas': self.ligacoes_ignoradas,
            'cnpj': self.cnpj,
            'ramo_empresa': self.ramo_empresa,
            'bu_do_cliente': self.bu_do_cliente,
            'faturamento_dolares': self.faturamento_dolares,
            'faturamento': self.faturamento,
            'qtd_funcionarios': self.qtd_funcionarios,
            'cliente_gavb': self.cliente_gavb,
            'setor_que_atendemos': self.setor_que_atendemos
        }
