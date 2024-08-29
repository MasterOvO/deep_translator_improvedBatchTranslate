# deep_translator_improvedBatchTranslate
-Much faster translating speed using deep_translator google translate

#improve version of deep_translator googletranslator .translate_batch function

#cause orignal batch_translate cant run >5000 character, and slow

#use mutiple thread to run faster

example of usage:

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
