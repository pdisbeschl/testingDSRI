

def main(config):
  
  if config.name == 'hello':
    print('bingo')
    
if __name__ == '__main__':
  args = get_parameters()
  print(args)
  main(args)
