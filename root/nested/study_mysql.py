import MySQLdb as mdb
import sys

con = None


def mapRadioButtonValues(x):
        return {
            'Yes': 'Y',
            'Y': 'Y',
            '1': 'Y',
            'No': 'N',
            'N': 'N',
            0: 'No',
        }.get(x, 'N')

try:
    con = mdb.connect('23.92.28.37', 'root', '', 'PRV2')
    cur = con.cursor(mdb.cursors.DictCursor)
    #cur.execute('''SELECT * FROM prv_supplierinfo WHERE id = %s''', '1')

    cur.execute('''SELECT field_value FROM prv_additionalfielddata WHERE field_id = %s AND supplier_id = %s''', (6, 1))

    #cur.execute('''SELECT id FROM prv_buyer WHERE buyer_name = %s''', 'SWA')

    rows = cur.fetchone()

    #desc = cur.description

    #print desc[1]
    #print "%s %3s %3s" % (desc[0][0], desc[1][0], desc[2][0])

    #for row in rows:
    #
    print rows['field_value']
    codes = rows['field_value']
    if len(codes) > 0:
        for code in codes.split(','):
            print "--"
            print code.strip()
    #print rows
    #print mapRadioButtonValues(rows['IS_COMP_PUBLICLY_TRADED'])
    #print rows['SECONDARY_NAICS_CODE']

except mdb.Error, e:

    print "Error %d: %s" % (e.args[0], e.args[1])

finally:

    if con:
        con.close()