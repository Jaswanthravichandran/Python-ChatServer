from colorama import Fore, Back, Style


ASCII_ART = Fore.RED + """                                                                                                            
   _|_|_|  _|    _|    _|_|    _|_|_|_|_|        _|_|_|  _|_|_|_|  _|_|_|    _|      _|  _|_|_|_|  _|_|_|    
 _|        _|    _|  _|    _|      _|          _|        _|        _|    _|  _|      _|  _|        _|    _|  
 _|        _|_|_|_|  _|_|_|_|      _|            _|_|    _|_|_|    _|_|_|    _|      _|  _|_|_|    _|_|_|    
 _|        _|    _|  _|    _|      _|                _|  _|        _|    _|    _|  _|    _|        _|    _|  
   _|_|_|  _|    _|  _|    _|      _|          _|_|_|    _|_|_|_|  _|    _|      _|      _|_|_|_|  _|    _|  
                                                                                                             
                                                                                                             """


#color = colored(ASCII_ART, 'red', attrs=['reverse', 'blink'])


def Server_Banner():
	print(Fore.RED + ASCII_ART)


def Client_Banner():
	print(ASCII_ART)


Server_Banner()