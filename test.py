import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')
file_handler = logging.FileHandler('sample.log')
file_handler.setLevel(logging.ERROR)
file_handler.setFormatter(formatter)
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
logger.addHandler(file_handler)
logger.addHandler(stream_handler)

test_str = 'Gfg is best . Gfg also has Classes now. Classes help understand better . '

print("The original string is : " + str(test_str))

repl_dict = {'Gfg': 'It', 'Classes': 'They'}

test_list = test_str.split(' ')
res = ' '.join([repl_dict.get(val) if val in repl_dict.keys() and test_list.index(val) != idx
                else val for idx, val in enumerate(test_list)])

# printing result
logger.debug('stri : {}'.format(test_str))
print("The string after replacing : " + str(res))
res1 = str(res)
logger.debug('final : {}'.format(res1))
