import ply.yacc as yacc

from file_reader import read_file
from amplenet_lexer import tokens
from server.server_controller import ServerController
from server.external_server import ExternalServer
from server.client import Client


controller = ServerController()


def p_process(p):
    '''
    process : create EXCLAMATION create EXCLAMATION join EXCLAMATION communication
            | join EXCLAMATION communication
    '''


def p_create_DEFAULT(p):
    '''
    create : DEFAULT LB ID RB
    '''
    controller.create_default(p[3])
    p[0] = p[3]


def p_create_EXTERNAL(p):
    '''
    create : EXTERNAL LB ID SEMICOLON NUMBER RB
    '''
    external = ExternalServer(p[3], p[5])
    external.start_recv()


def p_create_IP(p):
    '''
    create : OPEN LB ID SEMICOLON IP SEMICOLON NUMBER RB
    '''
    controller.create_server(p[3], p[5], p[7])


def p_client(p):
    '''
    client : CLIENT LB ID SEMICOLON IP SEMICOLON NUMBER RB
    '''
    client = Client(p[3], p[5], p[7])
    client.send_mode()


def p_join(p):
    '''
    join : CONNECT LB ID SEMICOLON ID RB
        | CONNECT LB create SEMICOLON create RB
    '''
    controller.connect_server(p[3], p[5])


def p_communication(p):
    '''
    communication : talk EXCLAMATION communication
                | talk EXCLAMATION
    '''


def p_talk(p):
    '''
    talk : SEND LB ID SEMICOLON ID SEMICOLON MESSAGE RB
    '''
    controller.send_message(p[3], p[5], p[7])


# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input at '%s', at line %s character %s." % (p.value, p.lineno, p.lexpos))


# Build the parser
parser = yacc.yacc()


if __name__ == '__main__':
    file_name = input("Enter name of file to execute: ")
    s = read_file("tests/%s.txt" % file_name)
    parser.parse(s)
