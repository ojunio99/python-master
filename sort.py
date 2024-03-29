#!/usr/bin/env python
# coding: utf-8

def sort_blocks():
    # First, we load the current README into memory
    with open('README.md', 'r') as read_me_file:
        read_me = read_me_file.read()

    # Separating the 'table of contents' from the contents (blocks)
    table_of_contents = ''.join(read_me.split('- - -')[0])
    blocks = ''.join(read_me.split('- - -')[1]).split('\n# ')
    for i in range(len(blocks)):
        if i == 0:
            blocks[i] = blocks[i] + '\n'
        else:
            blocks[i] = '# ' + blocks[i] + '\n'

    # Sorting the libraries
    inner_blocks = sorted(blocks[0].split('##'))
    for i in range(1, len(inner_blocks)):
        if inner_blocks[i][0] != '#':
            inner_blocks[i] = '##' + inner_blocks[i]
    inner_blocks = ''.join(inner_blocks)

    # Replacing the non-sorted libraries by the sorted ones and gathering all at the final_README file
    blocks[0] = inner_blocks
    final_README = table_of_contents + '- - -' + ''.join(blocks)

    with open('README.md', 'w+') as sorted_file:
        sorted_file.write(final_README)

def main():
    # First, we load the current README into memory as an array of lines
    with open('README.md', 'r') as read_me_file:
        read_me = read_me_file.readlines()

    blocks = []
    last_indent = None
    for line in read_me:
        s_line = line.lstrip()
        indent = len(line) - len(s_line)

        if any([s_line.startswith(s) for s in ['* [', '- [']]):
            if indent == last_indent:
                blocks[-1].append(line)
            else:
                blocks.append([line])
            last_indent = indent
        else:
            blocks.append([line])
            last_indent = None

    with open('README.md', 'w+') as sorted_file:
        # Then all of the blocks are sorted individually
        blocks = [
            ''.join(sorted(block, key=str.lower)) for block in blocks
        ]
        # And the result is written back to README.md
        sorted_file.write(''.join(blocks))

    # Then we call the sorting method
    sort_blocks()


if __name__ == "__main__":
    main()
