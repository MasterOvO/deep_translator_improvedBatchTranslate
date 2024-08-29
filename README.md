# deep_translator_improvedBatchTranslate
-Much faster translating speed using deep_translator google translate


-A function for faster translation using deep_translator google translater
-example of usage:
-"""
-#test for speed
-testing_lst = [f"你很快嗎, 我比較快{n}" for n in range(200)]
-slow_translator = GoogleTranslator(target="en")
-improve_translator = threading_googletranslator(target="en")

-start_time_slow = time.time()
-#a = slow_translator.translate_batch(testing_lst)
-end_time_slow = time.time()
-print("Runtime of original batch translator: ", end_time_slow-start_time_slow, "s")
-#runtime = 45s
-start_time_improve = time.time()
-b = improve_translator.improved_translate_batch(testing_lst, thread_count=10)
-end_time_improve = time.time()
-print(len(b))
-print("Runtime of improve batch translator: ", end_time_improve-start_time_improve, "s")
-#runtime = 0.01s
-"""
