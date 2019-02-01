"""

"""
from time import strftime


class MySQLTools:

    def label_machine(self, prefix='label', var_list=['var1', 'var2']):
        """
        Generates a text file with labeled values according to the
        prefix and names_list. Also this print the new list values.

        prefix: name of your data base or prefix
        names_list: a list you wish to label, every value will be labeled
        return: a new list with labeled values
        """

        # Build file
        file = open('labels_' + prefix + '_' + strftime("%d%m%y") + '.txt', 'a')

        # Generates a list
        new_list = []

        # Gives a list without label
        if prefix.lower() == 'null':
            for value in var_list:
                new_value = value + ','
                file.write(new_value + '\n')
                new_list.append(new_value)
                file.close()
            print('Done without label!')
            return new_list

        # Gives a list with labels
        else:
            for value in var_list:
                new_value = prefix + '.' + value + ','
                file.write(new_value + '\n')
                new_list.append(new_value)
                file.close()

            print('Labeled done!')

    def tab_stats(self, var_list, table, new_table, stats_of=0):
        """
        Generates a SQL code that creates a table with the amount of nulls
        or zeros by variable.

        var_list: Variables list
        table: Table where you wish to make the statistics of zeros
        new_table: Name of new table to store with statistics
        stats_of: 0 or 'null'
        return: A text file with SQL code
        """

        # Create file
        file = open('stats_' + str(stats_of) + '_' + table + '_' + strftime("%d%m%y") + '.sql', 'a')

        # String
        if stats_of == 0:
            col_name = 'total_ceros'
        else:
            stats_of = stats_of.lower()
            col_name = 'total_nulls'

        # SQL code comments
        file.write('--' + '=' * 50 + '\n')
        file.write(
            '-- Create ' + new_table + ' from ' + table + ' and gives the percentage of ' + str(stats_of) + 's\n')
        file.write('--' + '=' * 50 + '\n\n')

        # Create table
        file.write('CREATE TABLE' + ' ' + new_table + ' ' + 'AS\n')

        # Write code for every variable
        for num, var in enumerate(var_list):

            if stats_of == 0 or stats_of == 'null':

                # Writing SQL code
                sql_code = '-- Stats for {0} \n' \
                           'SELECT\n' \
                           '    \x27{0}\x27 AS var_name,\n' \
                           '    COUNT(*) AS total,\n'.format(var)
                file.write(sql_code)

                if stats_of == 0:
                    file.write('    SUM(CASE WHEN {} = 0 THEN 1 ELSE 0 END) AS total_ceros,\n'.format(var))
                elif stats_of == 'null':
                    file.write('    SUM(CASE WHEN {} IS NULL THEN 1 ELSE 0 END) AS total_nulls,\n'.format(var))

                file.write('    ({} / total) * 100 AS Porcentaje\n'.format(col_name))

                if num is not len(var_list) - 1:
                    file.write('FROM {} \nUNION ALL\n'.format(table))
                else:
                    file.write('FROM {};\n'.format(table))
            else:

                print('Please make sure that stats_of is equal to 0 or null!')

        file.close()
        print('SLQ code generated!')

    def fill_nulls_zeros(self, var_char=None, var_numeric=None, table='tab', new_table='new_tab'):
        """
            Generates a SQL code that creates a table and fill each null of a variable.
            If the variable is char the code fill with a word and if the variable is numeric
            the code fill with zero.
        """

        # Create file
        file = open('fill_nulls_and_zeros_{0}_{1}.sql'.format(table, strftime("%d%m%y")), 'a')

        # Comments
        file.write('--' + '=' * 80 + '\n')
        file.write('-- Create {0} from {1} and fill all nulls and zeros by \x27ND\x27 and 0s\n'.format(new_table, table))
        file.write('--' + '=' * 80 + '\n\n')

        # Create table
        file.write('CREATE TABLE {0} AS \nSELECT\n'.format(new_table))

        # Code to fill zeros
        try:
            # Write code for every variable of numeric type
            for num, num_var in enumerate(var_numeric):

                if var_char is not None:
                    file.write('    isnull({0}, 0) AS {0},\n'.format(num_var))
                else:
                    if num is not len(var_numeric) - 1:
                        file.write('    isnull({0}, 0) AS {0},\n'.format(num_var))
                    else:
                        file.write('    isnull({0}, 0) AS {0}\n'.format(num_var))

        except TypeError:

            print('Code for var_numeric was not written!')

        # Code to fill nulls
        try:

            # Write code for every variable of character type
            for num, var in enumerate(var_char):

                if num is not len(var_char) - 1:
                    file.write('    CASE WHEN {0} IS NULL THEN \x27{1}\x27 ELSE {0} END AS {0},\n'.format(var, 'ND'))
                else:
                    file.write('    CASE WHEN {0} IS NULL THEN \x27{1}\x27 ELSE {0} END AS {0}\n'.format(var, 'ND'))
        except TypeError:

            print('Code for var_char was not written!')

        file.write('FROM {};\n'.format(table))
        file.close()
        print('Nulls by zeros, SQL code generated!')