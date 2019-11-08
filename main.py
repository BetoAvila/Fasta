from Fasta import Fasta

print('\nHey, this is my Fasta class library!\nThanks for letting me participate!\n')

# Initial data input
path = ['C:/Git/Repos/Fasta/example.fasta']
f_inst = Fasta(path)
print('Here are some data of current fasta sequence:')
print(
    'Number of current sequences = {}\nList of all sequence indexes = {}\nDictionary of sequences =\n{}'.format(
        f_inst.count_seqs, f_inst.list_keys, f_inst.show_all_seqs))

# Adding new data
print('\n\nAdding new data')
f_inst.add_seqs(['>SEQUENCE_1',
                 'MTEITAAMVKELRESTGAGMMDCKNALSETNGDFDKAVQLLREKGLGKAAKKADRLAAEG',
                 'LVSVKVSDDFTIAAMRPSYLSYEDLDMTFVENEYKALVAELEKENEERRRLKDPNKPEHK',
                 'IPQFASRKQLSDAILKEAEEKIKEELKAQGKPEKIWDNIIPGKMNSFIADNSQLDSKLTL',
                 'MGQFYVMDDKKTVEQVIAEKEKEFGGKIKIVEFICFEVGEGLEKKTEDFAAEVAAQL',
                 '>SEQUENCE_2',
                 'SATVSEINSETDFVAKNDQFIALTKDTTAHIQSNSLQSVEELHSSTINGVKFEEYLKSQI',
                 'ATIGENLVVRRFATLKAGANGVVNGYIHTNGRVGVVIAAACDSAEVASKSRDLLRQICMH'])
print(
    'Number of current sequences: {}\nList of all sequence indexes: {}\nDictionary of sequences:\n{}'.format(
        f_inst.count_seqs, f_inst.list_keys, f_inst.show_all_seqs))

# Delete sequences
print('\n\nDeleting data')
f_inst.del_seqs([1, 3])
print(
    'Number of current sequences: {}\nList of all sequence indexes: {}\nDictionary of sequences:\n{}'.format(
        f_inst.count_seqs, f_inst.list_keys, f_inst.show_all_seqs))

# Picking the remaining two:
print('\n\nPicking remaining two')
print(
    f_inst.sequence([2, 4])
)
print('Thanks!  :D\n\t\t\t\t- Beto Avila\n\t\t\t\t[8 nov 2019]')
