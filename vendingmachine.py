from fire import Fire

from vm_gen import create_graph

DEFAULT_OUT = 'vending_machine.dot'


def report(total, increments, initial, n, e):
    print(f'''
--- Input ---
Target: {total}
Increments: {increments}
Initial: {initial}

--- Solution ---
No. of nodes: {len(n)}
No. of edges: {len(e)}

Nodes: {n}
Edges: {e}
'''.lstrip())


class VendingMachineGenerator:
    @staticmethod
    def save(target, increments, initial=0, out=DEFAULT_OUT):
        g, n, e = create_graph(target, increments, initial)
        g.save(filename=out)

        report(target, increments, initial, n, e)

    @staticmethod
    def render(target, increments, initial=0, out=DEFAULT_OUT, view=False):
        g, n, e = create_graph(target, increments, initial)
        g.render(filename=out, view=view)

        report(target, increments, initial, n, e)


if __name__ == '__main__':
    Fire(VendingMachineGenerator)
