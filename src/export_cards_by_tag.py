#
# export_cards_by_tag.py <simon.greuter@gmx.net>
#

import sys
import getopt
import copy
from mnemosyne.script import Mnemosyne

# 'data_dir = None' will use the default system location, edit as appropriate.
data_dir = None

def collect_tags(db):
    tags = set()
    for _card_id, _fact_id in db.cards():
        card = db.card(_card_id, is_id_internal=True)
        tags = tags | set([tag for tag in card.tags])
    return tags

def process_string_for_text_export(text):
    text = text.encode("utf-8").replace("\n", "<br>").replace("\t"," ")
    if text == "":
        text = "<br>"
    return text

def export_cards(db, output_path, _tag):
    filename = output_path + _tag.name.replace("::", "_") + ".txt"
    outfile = file(filename, "w")

    for _card_id, _fact_id in db.cards():
        card = db.card(_card_id, is_id_internal=True)
        if _tag in card.tags:
            q = process_string_for_text_export(\
                    card.question(render_chain="plain_text"))
            a = process_string_for_text_export(\
                    card.answer(render_chain="plain_text"))
            outfile.write("%s\t%s\n" % (q, a))

# find the set of all tags, then export all cards per tag;
# surely not the most efficient way to do it..

def main(argv):
    output_path = ''

    try:
        opts, args = getopt.getopt(argv,"ho:",["help","opath="])
    except getopt.GetoptError:
        print 'export_cards_by_tag.py -o <outputpath>'
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print 'export_cards_by_tag.py -o <outputpath>'
            sys.exit()
        elif opt in ("-o", "--opath"):
            output_path = arg

    mnemosyne = Mnemosyne(data_dir)
    for _tag in collect_tags(mnemosyne.database()):
        export_cards(mnemosyne.database(), output_path, _tag)
    mnemosyne.finalise()

if __name__ == "__main__":
   main(sys.argv[1:])
