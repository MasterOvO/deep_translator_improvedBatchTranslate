from deep_translator import GoogleTranslator
import time
import threading


#improve version of deep_translator googletranslator .translate_batch function
#cause orignal batch_translate cant run >5000 character, and slow
#use mutiple thread to run faster
class threading_googletranslator(GoogleTranslator):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.running_threads = []

    def improved_translate_batch(self, list_to_translate, thread_count=4):
        #list_to_translate: list for translation
        #split_lst_path: temp directory for storing split list translation checkpoint
        #thread_count: number of thread to run, more=faster, but may get ban feel free to experiment           
        self.result_dict = {}
        result_lst = []
        def _batchTranslate(lst,i):
            max_char = 5000
            result_lst = []
            translator = GoogleTranslator(self.source,self.target)
            n = 0
            m = len(lst)
            if len(lst[0]) >= max_char:
                print(f"Single input is larger that Max character available {max_char}!")
                self.result_dict[i] = []
                return 
            while len(self._flatten(result_lst)) < len(lst):
                split_lst = lst
                if n==len(lst)-1: #last item
                    split_lst = [lst[-1]]
                else:
                    while len(self._flatten(split_lst)) > max_char:
                        m=m-1
                        split_lst = lst[n:m]
                #print("exceed char limit, split list for thread ", i+1)
                print(f"Translating {(i+1)*n}-{(i+1)*m}")
                result_lst.append(translator.translate_batch(split_lst))
                #reset after appending
                n=m
                m=len(lst)
            self.result_dict[i] = self._flatten(result_lst)


        for n in range(thread_count):
            split_lst = list_to_translate[int(len(list_to_translate)/thread_count)*n: int(len(list_to_translate)/thread_count)*(n+1)\
                                            if n!=(thread_count-1) else len(list_to_translate) ]
            #print(n) #for some reason this line is nessary
            t = threading.Thread(target=_batchTranslate, args = (split_lst,n))
            t.start()
            self.running_threads.append(t)
        
        for t in self.running_threads:
            t.join()

        for i in range(thread_count):
            result_lst.append(self.result_dict[i])
        return self._flatten(result_lst)


    def _flatten(self, xss):
            return [x for xs in xss for x in xs]
        
    

"""
#test for speed
testing_lst = [f"你很快嗎, 我比較快{n}" for n in range(200)]
slow_translator = GoogleTranslator(target="en")
improve_translator = threading_googletranslator(target="en")

start_time_slow = time.time()
#a = slow_translator.translate_batch(testing_lst)
end_time_slow = time.time()
print("Runtime of original batch translator: ", end_time_slow-start_time_slow, "s")
#runtime = 50s
start_time_improve = time.time()
b = improve_translator.improved_translate_batch(testing_lst, thread_count=10)
end_time_improve = time.time()
print(b)
print("Runtime of improve batch translator: ", end_time_improve-start_time_improve, "s")
#runtime = 7s
"""






