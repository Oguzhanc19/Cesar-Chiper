# Türkçe için büyük ve küçük harfler
turkceHarfKucuk = "abcçdefgğhıijklmnoöprsştuüvyz"
turkceHarfBuyuk = "ABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZ"

def caesar(sifreli_metin, key):
    decrypted_text = ""
    
    for char in sifreli_metin:
        if char in turkceHarfKucuk:
            # Küçük harf için işlem
            index = turkceHarfKucuk.index(char)
            shifted_index = (index - key) % len(turkceHarfKucuk)
            decrypted_text += turkceHarfKucuk[shifted_index]
        elif char in turkceHarfBuyuk:
            # Büyük harf için işlem
            index = turkceHarfBuyuk.index(char)
            shifted_index = (index - key) % len(turkceHarfBuyuk)
            decrypted_text += turkceHarfBuyuk[shifted_index]
        else:
            # Harf değilse olduğu gibi ekle (boşluk, noktalama işaretleri vs.)
            decrypted_text += char

    return decrypted_text

# Kullanıcıdan key alma (Key=17)
key = int(input("Lütfen şifre çözmek için kaydırma miktarını (key) girin: "))

# Şifrelenmiş metin
sifreli_metin = "Uşdşğoc Bjijnel, ohbşğcşğzdş sfdşğşb edcoğy holoıyd neğcjbcoğydo boğıy vonyğcoçomo rocyıymeğsj. Edjd ufnkdsş, notşğsşd sovo fdşçcz ecod ışm ohbşğcşğzdzd çeğoczdz mkbhşb ijiçobiy. Edcoğo uklşd lşğzpz özğbor hfn hfmcşmzg uşğz rşbzcsz."

# Şifre çözme key=17 ile metin çözülüyor.
decrypted_text = caesar(sifreli_metin, key)
print(f"Kaydırma miktarı (key): {key}")
print("Çözülmüş metin:")
print(decrypted_text)