class Fasta:
    """
    Fasta class crated to manipulate .fasta files. Such files are designed to store and
    manipulate DNA data, please refer to: https://en.wikipedia.org/wiki/FASTA_format.
    This class allows you to read .fasta files or type sequences directly in class'
    inputs as described in :param section. For this explanation an arbitrary
    instance of Fasta class will be referred as f_inst, thus f_inst has the following:

    Attributes
        f_inst.count_seqs - read-only (int) describing how many sequences exist in f_inst
        f_inst.list_keys - read-only (list) that shows the numbers (or indexes) of
            existing sequences
        f_inst.show_all_seqs - read-only (dict) that stores and manipulates data

    Methods
        f_inst.sequence(keys) - Returns as (str) the sequence or sequences whose keys are
            listed in (list) of (int) keys
        f_inst.del_seqs(keys) - Deletes sequence or sequences according to (int) listed in
         (list) keys
        f_inst.add_seqs(input_data) - Appends new data in the form of (list) of sequences
            as (str); similarly as 'input_data' variable while instantiating Fasta class

    :rtype: Fasta class instance
    :param input_data (list) containing .fasta file location path, or sequences as (str).
        When using path option the list most be of length 1 and containing the path as a string,
        i.e. inputs = ['C:/here/there/example.fasta'].
        When typing sequences such must follow the format:
        inputs = ['>SEQUENCE_1', 'MTEI...', 'VKEL...', ..., '>SEQUENCE_2', ...,] where every
        element of the list except for the ones which start with '>SEQUENCE_' are rows of
        the sequence.
    """

    def __init__(self, input_data):
        if '>SEQUENCE_' in input_data[0]:
            seq_num = 0
            d_seqs = dict()
            for i in range(len(input_data)):
                if '>SEQUENCE_' in input_data[i]:
                    seq_num += 1
                if ('>SEQUENCE_' not in input_data[i]) & ('\n' not in input_data[i]) & ('' != input_data[i]):
                    if seq_num in d_seqs:
                        d_seqs[seq_num].append(input_data[i])
                    if seq_num not in d_seqs:
                        d_seqs[seq_num] = [input_data[i]]
        if '/' in input_data[0]:
            data = open(input_data[0]).read().split('\n')
            seq_num = 0
            d_seqs = dict()
            for i in range(len(data)):
                if '>SEQUENCE_' in data[i]:
                    seq_num += 1
                if ('>SEQUENCE_' not in data[i]) & ('\n' not in data[i]) & ('' != data[i]):
                    if seq_num in d_seqs:
                        d_seqs[seq_num].append(data[i])
                    if seq_num not in d_seqs:
                        d_seqs[seq_num] = [data[i]]
        self._num_seqs = int(len(d_seqs))
        self._d_seqs = d_seqs
        self._seqs = list(d_seqs)

    @property
    def count_seqs(self):
        return self._num_seqs

    @property
    def show_all_seqs(self):
        return self._d_seqs

    @property
    def list_keys(self):
        return self._seqs

    def sequence(self, keys):
        """
        Returns as (str) the sequence or sequences whose keys are listed
        :param keys:(list) of (int) defining the sequence or sequences you want to retreive
        :return: (str) sequence or sequences of Fasta class instance
        """
        out = ''
        for j in range(len(keys)):
            out += '>SEQUENCE_{}'.format(keys[j]) + '\n'
            for i in range(len(self._d_seqs[keys[j]])):
                out += self._d_seqs[keys[j]][i] + '\n'
        return out

    def del_seqs(self, keys):
        """
        Deletes sequence or sequences according to listed integers in (list) keys
        :param keys: (list) of integers of sequences to delete
        :return: Nothing, instead modifies existing instance
        """
        for j in range(len(keys)):
            del self._d_seqs[keys[j]]
        self._num_seqs = int(len(self._d_seqs))
        self._d_seqs = self._d_seqs
        self._seqs = list(self._d_seqs)

    def add_seqs(self, input_data):
        """
        Method to add new sequences to Fasta class instance. Sequences must follow the format:
        input_data = ['>SEQUENCE_1', 'MTEI...', 'VKEL...', ..., '>SEQUENCE_2', ...,] where
        every element of the list except for the ones which start with '>SEQUENCE_' are rows
        of the sequence.
        :param input_data: (list) containing one or more sequences
        :return: Nothing, instead modifies existing instance
        """
        seq_num = self.list_keys[-1]
        d_seqs = self._d_seqs
        for i in range(len(input_data)):
            if '>SEQUENCE_' in input_data[i]:
                seq_num += 1
            if ('>SEQUENCE_' not in input_data[i]) & ('\n' not in input_data[i]) & ('' != input_data[i]):
                if seq_num in d_seqs:
                    d_seqs[seq_num].append(input_data[i])
                if seq_num not in d_seqs:
                    d_seqs[seq_num] = [input_data[i]]
        self._num_seqs = int(len(self._d_seqs))
        self._d_seqs = self._d_seqs
        self._seqs = list(self._d_seqs)

