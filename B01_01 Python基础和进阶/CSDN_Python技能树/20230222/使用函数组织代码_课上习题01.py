def dump(index, default=0, *args, **kw):
    print('index:', index)
    print('default:', default)
    for i, arg in enumerate(args):
        print(f'arg[{i}]:', arg)
    for key,value in kw:
        print(f'keyword_argument{key}:{value}')
    print('')

if __name__=='__main__':
    dump(0)
    dump(0,2)
    dump(0,2,"Hello","World")
    dump(0,2,"Hello","World", install='Python', run='Python Program')



