base =  {'A':set(['B','C']),
         'B':set(['A','H','J',]),
         'C':set(['A','D','G']),
         'D':set(['C','E']),
         'E':set(['D','F']),
         'F':set(['E','G','K','L']),
         'G':set(['C','F']),
         'H':set(['B','I']),
         'I':set(['H','J','K']),
         'J':set(['B','I']),
         'K':set(['F','I','L']),
         'L':set(['F','K'])}
    

def dfs(graf, mulai, tujuan):
    queue = [[mulai]]
    visited = set()

    while queue:
        panjang = len(queue)-1
        # masukkan antrian paling depan ke variabel jalur
        jalur = queue.pop(panjang)

        # simpan node yang dipilih ke variabel state, misal jalur = C,B maka simpan B ke variabel state
        state = jalur[-1]

        # cek state apakah sama dengan tujuan, jika ya maka return jalur
        if state == tujuan:
            return jalur
        # jika state tidak sama dengan tujuan, maka cek apakah state tidak ada di visited
        elif state not in visited:
            # jika state tidak ada di visited maka cek cabang
            for cabang in graf.get(state, []): #cek semua cabang dari state
                jalur_baru = list(jalur) #masukkan isi dari variabel jalur ke variabel jalur_baru
                jalur_baru.append(cabang) #update/tambah isi jalur_baru dengan cabang
                queue.append(jalur_baru) #update/tambah queue dengan jalur_baru

            # tandai state yang sudah dikunjungi sebagai visited
            visited.add(state)

        #cek isi antrian
        isi = len(queue)
        if isi == 0:
            print("Tidak ditemukan")
