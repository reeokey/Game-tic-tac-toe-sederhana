def papan_game(papan):
    print("-------------")
    for i in range(3):
        print("|", papan[i*3], "|", papan[i*3+1], "|",papan[i*3+2], "|")
        print("-------------")

def periksa_kemenangan(papan):
    # cek baris
    for i in range(3):
        if papan[i*3] == papan[i*3+1] == papan[i*3+2] != " ":
            return papan[i*3]
    # cek kolom
    for i in range(3):
        if papan[i] == papan[i+3] == papan[i+6] != " ":
            return papan[i]
        # cek diagonal
        if papan[0] == papan[4] == papan[8] != " ":
            return papan[0]
        if papan[2] == papan[4] == papan[6] != " ":
            return papan[2]
        return None

def main():
    papan = [" " for _ in range(9)]
    pemain1 = input("Nama Pemain 1: ")
    pemain2 = input("Nama Pemain 2: ")
    gerak_pemain = pemain1
    
    while True:
        papan_game(papan)
        
        #input posisi
        jalan = int(input(f"{gerak_pemain},Masukkan Posisi (1-9): "))-1
        
        if papan[jalan] == " ":
            papan[jalan] = "X" if gerak_pemain == pemain1 else "O"
            
            pemenang = periksa_kemenangan(papan)
            if pemenang:
                papan_game(papan)
                if pemenang == "X":
                    print(f"Selamat, {pemain1} menang!")
                else:
                    print(f"Selamat, {pemain2} menang!")
                break
            
            if " " not in papan:
                papan_game(papan)
                print("Permainan Seri!")
                break
            
            gerak_pemain = pemain2 if gerak_pemain == pemain1 else pemain1
        else:
            print("Posisi Sudah Terisi, Coba Lagi")

if __name__ == "__main__":
    main()