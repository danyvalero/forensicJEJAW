import subprocess
from datetime import datetime
from io import open


def print_logo():
    """
    print out the logo and version information
    """
    
    print(""" 
          
                    WWWWWWWWWWWWWWWWWWWWWNWWWWWWWWWNWWNWXo''';o0NWNkc,''';xNWWNWWWWWWWWWWWWWWWWWWWWWWWWWNWWWWWWWWWWWWWWW
                    WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWXl;dOOxoclolcokO0Ol;xNWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
                    WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWNd,xNWWWWX0k0NWWWWWXl;0WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
                    WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWK::KWWWWWWWWWWWWWWWWO;oNWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
                    WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWNXx':KNWWWWWWWWWWWWWWNk';ONWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
                    WWWWWWWWWWWWWWWWWWWWWWWWWWWWWNKdc'   .;ldxOO000Okxdoc,.  .;oOXWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
                    WWWWWWWWWWWWWWWWWWWWWWWWWWWWNk;cxo'.        ...         .;dd:lKWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
                    WWWWWWWWWWWWWWWWWWWWWWWWWWWWNd,dXWXOdc;'..      ....';lx0NWKc;OWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
                    WWWWWWWWWWWWWWWWWWWWWWWWWWWWWXxccox0KXNXK0OkkkkkOKKKXNXKOdlclONWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
                    WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWN0d'..';:clooooooolcc:;'..:kKNWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
                    WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWNl                     .xWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
                    WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWk.                    ;KWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
                    WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWNl                   .kWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
                    WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWXl.                .xNWWWWWWWWWWNNNNWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
                    WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWXx'             .:ONWWWWWWNKkl:,'',:lxKWWWWWWWWWWWWWWWWWWWWWWWWW
                    WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWKd:.      .';cONWWWWWWW0l. .':cc:,. .l0WWWWWWWWWWWWWWWWWWWWWWW
                    WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWXkddxxdddxxdod0NWWWWWWk' .l0NWWWWN0o. 'kNWWWWWWWWWWWWWWWWWWWWW
                    WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWXOo'  .;xXWKo'   .;xKNWW0, .kNWWWWWWWWNk' ,0WWWWWWWWWWWWWWWWWWWWW
                    WWWWWWWWWWWWWWWWWWWWWWWWWWWWWNX0xl:'.       ,:.        .,oXx. cNWWWWWWWWWWNc .dWWWWWWWWWWWWWWWWWWWWW
                    WWWWWWWWWWWWWWWWWWWWWWWWWXOxl;..                         'Ok. :XWWWWWWWWWWX: .xWWWWWWWWWWWWWWWWWWWWW
                    WWWWWWWWWWWWWWWWWWWWWWWXo'.                               l0c .lKWWWWWWWWKc. cXWWWWWWWWWWWWWWWWWWWWW
                    WWWWWWWWWWWWWWWWWWWWWWXl                                  :KK;  'cxO0K0xl. .lKWWWWWWWWWWWWWWWWWWWWWW
                    WWWWWWWWWWWWWWWWWWWWWWk.                                'dOx:.   ........,lONWWWWWWWWWWWWWWWWWWWWWWW
                    WWWWWWWWWWWWWWWWWWWWWNl                               .l0x,    .dOxddddk0NWWWWWWWWWWWWWWWWWWWWWWWWWW
                    WWWWWWWWWWWWWWWWWWWWWK;                              ,kOc.    .xXx;;cONWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
                    WWWWWWWWWWWWWWWWWWWWWO'                             ;0x.     ;OKo.   cXWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
                    WWWWWWWWWWWWWWWWWWWWWk.                             lKc    .dKk,     ;KWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
                    WWWWWWWWWWWWWWWWWWWWNx.                            .:KO;..;ONO,      ;KMWWWWWWWWWWWWWWWWWWWWWWWWWWWN
                                                                                                                    
                    8 8888888888       ,o888888o.     8 888888888o.   8 8888888888   b.             8    d888888o.    8 8888     ,o888888o.    
                    8 8888          . 8888     `88.   8 8888    `88.  8 8888         888o.          8  .`8888:' `88.  8 8888    8888     `88.  
                    8 8888         ,8 8888       `8b  8 8888     `88  8 8888         Y88888o.       8  8.`8888.   Y8  8 8888 ,8 8888       `8. 
                    8 8888         88 8888        `8b 8 8888     ,88  8 8888         .`Y888888o.    8  `8.`8888.      8 8888 88 8888           
                    8 888888888888 88 8888         88 8 8888.   ,88'  8 888888888888 8o. `Y888888o. 8   `8.`8888.     8 8888 88 8888           
                    8 8888         88 8888         88 8 888888888P'   8 8888         8`Y8o. `Y88888o8    `8.`8888.    8 8888 88 8888           
                    8 8888         88 8888        ,8P 8 8888`8b       8 8888         8   `Y8o. `Y8888     `8.`8888.   8 8888 88 8888           
                    8 8888         `8 8888       ,8P  8 8888 `8b.     8 8888         8      `Y8o. `Y8 8b   `8.`8888.  8 8888 `8 8888       .8' 
                    8 8888          ` 8888     ,88'   8 8888   `8b.   8 8888         8         `Y8o.` `8b.  ;8.`8888  8 8888    8888     ,88'  
                    8 8888             `8888888P'     8 8888     `88. 8 888888888888 8            `Yo  `Y8888P ,88P'  8 8888     `8888888P'    
                   """)
    print('\n')
    print('----------------------(version', '1.0' ,')----------------------\n')
    print('The source code is available at https://github.com/danyvalero/forensicJEJAW.git')
    print('Developed by Wilson Barios, Jorge Ortiz, Jose Torregroza y Daniel Valero \'s Team Forensic JEJAW\n')
print_logo()


def menu ():
    print('1. Análisis Memoria RAM')
    print('2. Huella Digital')
    print('3. Forense')
    selection = input('Seleccione la herramienta que desee ejecutar (1, 2 o 3): ')
    
    if selection == '1':
        try:
            fichero = open ('.//Result/ejecucion_programa.txt', 'a', encoding='utf-8')                
            date = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
            software_name = input ('Escribe nombre del programa a ejecutar: ')
            run_date = 'Se ejecuto el programa ' + software_name + ' con la fecha del computador: ', date
            print(run_date)
            file = ".//Tools Ram/" + software_name
            fichero.writelines(run_date)
            path_program = subprocess.Popen([file], stdout=fichero, stderr=subprocess.PIPE, universal_newlines=True)          
            out, err = path_program.communicate(timeout=10)
            exit_code = path_program.returncode
            fichero.writelines('\n' + file + '\n')
            fichero.close()
        except:
            print('programa no existe o necesita alguna bandera para ejeuctarse, consulte ayuda con -h en el programa disponible')
    elif selection == '2':
        try:
            fichero = open ('.//Result/ejecucion_programa.txt', 'a', encoding='utf-8')                
            date = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
            print('Genera y compara el Hash de los archivos que necesite con estos dos programas: HashMyFiles y md5summer')
            software_name = input ('Escribe nombre del programa a ejecutar: ')
            run_date = 'Se ejecuto el programa ' + software_name + ' con la fecha del computador: ', date
            print(run_date)
            file = ".//Hash/" + software_name
            fichero.writelines(run_date)
            path_program = subprocess.Popen(file)          
            out, err = path_program.communicate(timeout=10)
            exit_code = path_program.returncode
            fichero.writelines('\n' + file + '\n')
            fichero.close()
        except:
            print('programa no existe o necesita alguna bandera para ejeuctarse, consulte ayuda con -h en el programa disponible')
    elif selection == '3':
        try:
            fichero = open ('.//Result/ejecucion_programa.txt', 'a', encoding='utf-8')                
            date = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
            software_name = input ('Escribe nombre del programa a ejecutar: ')
            run_date = 'Se ejecuto el programa ' + software_name + ' con la fecha del computador: ', date
            print(run_date)
            file = ".//Forense/" + software_name
            fichero.writelines(run_date)
            path_program = subprocess.Popen(file)          
            out, err = path_program.communicate(timeout=10)
            exit_code = path_program.returncode
            fichero.writelines('\n' + file + '\n')
            fichero.close()
        except:
            print('programa no existe o necesita alguna bandera para ejeuctarse, consulte ayuda con -h en el programa disponible')
    else:
        print('Opción Invalida')
print(menu())
