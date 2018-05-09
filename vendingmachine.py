from fire import Fire

from vm_gen import create_graph


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
    def save(total, increments, initial=0, out='vendingmachine.dot'):
        g, n, e = create_graph(total, increments, initial)
        g.save(filename=out)

        report(total, increments, initial, n, e)

    @staticmethod
    def render(total, increments, initial=0, out='vendingmachine.dot', view=False):
        g, n, e = create_graph(total, increments, initial)
        g.render(filename=out, view=view)

        report(total, increments, initial, n, e)


if __name__ == '__main__':
    Fire(VendingMachineGenerator)
