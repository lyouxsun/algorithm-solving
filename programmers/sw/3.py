def solution(table, search):
      answer = 0
      
      attributes = table[0].split()
      d = dict()
      idx = 0
      for i in attributes:
            d[i] = idx
            idx += 1
      
      data = []
      for i in range(1, len(table)):
            data.append(table[i].split())
            keywords = search.split()
      
      while keywords:
            new_data = []
            attribute = keywords.pop(0)
            option = keywords.pop(0)
      
      for i in data:
            if i[d[attribute]] == option:
                  new_data.append(i)
                  data = new_data
                  # print('data=', data)
                  answer += len(data)
      
      return answer