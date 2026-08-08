<div align="center">
  <h1>🔐 Caesar Cipher Algorithm</h1>
  <p><i>Advanced Caesar Cipher Implementation with Native Turkish Alphabet Support<br>Yerleşik Türkçe Alfabe Destekli Gelişmiş Sezar Şifrelemesi</i></p>
  ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
</div>

<br>

## 🇬🇧 English

Unlike basic Caesar Cipher scripts that rely on the ASCII table (which breaks when encountering non-English characters), this Python implementation is purpose-built to flawlessly handle the **Turkish Alphabet**.

### 🧠 Cryptographic Logic
- **Custom Alphabet Arrays**: Defines explicit strings for Turkish characters (`turkceHarfKucuk = "abcçdefgğhıijklmnoöprsştuüvyz"`).
- **Modulo Arithmetic Validation**: When encrypting or decrypting, the script finds the exact index of the character, applies the shift (Key), and calculates `(index - key) % length_of_alphabet`. This prevents index-out-of-bounds errors and ensures proper wrapping from 'z' back to 'a'.
- **Case & Symbol Preservation**: The algorithm intelligently checks if a character is uppercase or lowercase and processes it accordingly. If the character is a space or punctuation mark, it bypasses the cipher, preserving the sentence structure.

### 🚀 Usage
Simply input your ciphered text and provide the shift key (e.g., `key = 17`). The script will output the human-readable text immediately.

---

## 🇹🇷 Türkçe

Sadece İngilizce karakterleri destekleyen ve ASCII tablosu üzerinden kaydırma yaptığı için Türkçe karakterlerde çöken basit Sezar Şifreleme (Caesar Cipher) kodlarının aksine; bu proje **Türk alfabesini eksiksiz ve hatasız işlemek üzere** özel olarak geliştirilmiştir.

### 🧠 Kriptografik Mantık
- **Özel Alfabe Dizileri**: Türkçe karakterleri içeren dizeleri açıkça tanımlar (`turkceHarfKucuk = "abcçdefgğhıijklmnoöprsştuüvyz"`).
- **Modüler Aritmetik Doğrulaması**: Şifreleme veya çözme yaparken harfin indeksini bulur, kaydırma miktarını (Key) uygular ve `(index - key) % alfabe_uzunluğu` formülü ile modül işlemi yapar. Bu sayede 'z' harfinden sonra tekrar 'a' harfine dönüş kusursuz sağlanır.
- **Büyük/Küçük Harf ve Sembol Koruması**: Algoritma, harfin büyük mü yoksa küçük mü olduğunu tespit ederek ilgili alfabede işlem yapar. Boşluk veya noktalama işaretleri şifrelenmeden olduğu gibi bırakılır, böylece cümle yapısı bozulmaz.

### 🚀 Kullanım
Şifreli metni programa yapıştırın ve kaydırma miktarını (Örn: `key = 17`) girin. Betik saniyeler içinde çözülmüş Türkçe metni ekrana basacaktır.
