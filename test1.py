import logging
logging.basicConfig(filename="log.txt",level=logging.DEBUG,format='%(asctime)s %(levelname)s %(name)s %(message)s')

class string_task:

    def string_extraction(self,in_str):
        logging.info("entered string extraction ")
        self.in_str = in_str
        try :
            logging.info("inside try block of string extraction")
            if len(in_str)==0 :
                logging.info(" string is empty")
                raise ValueError("empty error")
            else :
                logging.info("string not empty")
                str = in_str[::3]
                return str
        except Exception as e:
            logging.exception(e)

    def string_reverse(self,in_str):
        logging.info("entered string reverse")
        try :
            if len(in_str) == 0 :
                logging.info("string is empty")
                raise ValueError("empty error")
            else :
                logging.info("string not empty")
                str = in_str[::-1]
                return str
        except Exception as e:
            logging.exception(e)

    def string_split(self,in_str):
        logging.info("entered string split ")
        try :
            if len(in_str) == 0 :
                logging.info("string is empty")
                raise ValueError("empty error")
            else :
                logging.info("string not empty")
                str = in_str.split()
                return str
        except Exception as e:
            logging.exception(e)

    def string_Upper(self,in_str):
        logging.info("entered string upper ")
        try :
            if len(in_str) == 0 :
                logging.info("string is empty")
                raise ValueError("empty error")
            else :
                logging.info("string not empty")
                str = in_str.upper()
                return str
        except Exception as e:
            logging.exception(e)

    def string_lower(self,in_str):
        logging.info("entered string lower ")
        try :
            if len(in_str) == 0 :
                logging.info("string is empty")
                raise ValueError("empty error")
            else :
                logging.info("string not empty")
                str = in_str.lower()
                return str
        except Exception as e:
            logging.exception(e)

    def string_title(self,in_str):
        logging.info("entered string title ")
        try :
            if len(in_str) == 0 :
                logging.info("string is empty")
                raise ValueError("empty error")
            else :
                logging.info("string not empty")
                str = in_str.title()
                return str
        except Exception as e:
            logging.exception(e)

class list_task():

    def list_reverse(self,in_list):
        logging.info("entered list reverese ")
        try :
            if len(in_list) == 0 :
                logging.info("list is empty")
                raise ValueError("empty error")
            else :
                logging.info("list is  not empty")
                in_list.reverse()
                return in_list
        except Exception as e:
            logging.exception(e)

akh = string_task()
lav = list_task()
l = [1,2,3,4,5]

print(lav.list_reverse(l))
print(akh.string_extraction("With Ginger's Sentence Rephraser you can now express yourself better everywhere you write. Spice up your text with new variations for your sentences; add synonyms,"))
print(akh.string_reverse("With Ginger's Sentence Rephraser you can now express yourself better everywhere you write. Spice up your text with new variations for your sentences; add synonyms,"))
print(akh.string_split("With Ginger's Sentence Rephraser you can now express yourself better everywhere you write. Spice up your text with new variations for your sentences; add synonyms,"))
print(akh.string_lower("With Ginger's Sentence Rephraser you can now express yourself better everywhere you write. Spice up your text with new variations for your sentences; add synonyms,"))
print(akh.string_Upper("With Ginger's Sentence Rephraser you can now express yourself better everywhere you write. Spice up your text with new variations for your sentences; add synonyms,"))
print(akh.string_title("With Ginger's Sentence Rephraser you can now express yourself better everywhere you write. Spice up your text with new variations for your sentences; add synonyms,"))
