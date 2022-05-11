# =============================================================================
# Praštevila in racionalna števila
# =====================================================================@009867=
# 1. podnaloga
# Sestavite (neskončen) generator `prastevila(n)`, ki bo kot argument
# dobil naravno število `n` in vračal praštevila, začenši z najmanjšim
# praštevilom, ki je strogo večje od `n`.
# 
#     >>> g = prastevila(1)
#     >>> for p in g:
#     ...     if p > 30:
#     ...         break
#     ...     print(p)
#     ...
#     2
#     3
#     5
#     7
#     11
#     13
#     17
#     19
#     23
#     29
#     >>> [next(g) for i in range(10)] # next(g) vrne naslednji člen generatorja, to ponovimo 10-krat
#     [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
# =============================================================================
def je_prastevilo(p):
    i = 2
    while i ** 2 <= p:
        if p % i == 0:
            return False
        i += 1
    return True

def prastevila(n):
    p = n + 1
    while True:
        if je_prastevilo(p):
            yield p
        p += 1

# =====================================================================@009868=
# 2. podnaloga
# Sestavili bomo generator `pozitivna_racionalna()`, ki bo vračal
# pozitivna racionalna števila.
# 
# Mislimo si neskončno matriko, ki ima v $i$-ti vrstici in $j$-tem stolpcu
# ulomek $\frac{j}{i}$:
# 
# $\begin{pmatrix}
# \frac{1}{1} & \frac{2}{1} & \frac{3}{1} & \frac{4}{1} & \frac{5}{1} & \dots \\ 
# \frac{1}{2} & \frac{2}{2} & \frac{3}{2} & \frac{4}{2} & \frac{5}{2} & \dots \\ 
# \frac{1}{3} & \frac{2}{3} & \frac{3}{3} & \frac{4}{3} & \frac{5}{3} & \dots \\ 
# \frac{1}{4} & \frac{2}{4} & \frac{3}{4} & \frac{4}{4} & \frac{5}{4} & \dots \\
# \frac{1}{5} & \frac{2}{5} & \frac{3}{5} & \frac{4}{5} & \frac{5}{5} & \dots \\    
# \vdots & \vdots & \vdots & \vdots & \vdots & \ddots \\ 
# \end{pmatrix}$
# 
# V takšni neskončni matriki se nahajajo vsa pozitivna racionalna števila.
# Torej se moramo na nek _primeren način_ sprehoditi po elementih te matrike,
# pri čemer pa moramo biti pazljivi, saj se vsako racionalno število v takšni
# matriki pojavlja znova in znova. Na primer ulomki
# 
# $\frac{1}{3}, \frac{2}{6}, \frac{3}{9}, \frac{4}{12}, \ldots$
# 
# vsi predstavljajo isto racionalno število. Med vse temi ulomki pa je
# natanko en _okrajšan_ ulomek. Če se torej sprehodimo po vseh ulomkih v
# tej matriki in ignoriramo tiste, ki niso okrajšani, bomo vsako pozitivno
# racionalno število obiskali natanko enkrat.
# 
# Kako pa naj se na _primeren način_ sprehodimo po tej matriki? Če bi
# šli po prvi vrstici, bi obiskali samo naravna števila. Do ostalih ne
# bi nikoli prišli, saj je že naravnih števil neskončno. Če pa gremo po
# diagonalah, potem vsako število slej ko prej pride na vrsto. _Primeren_
# vrstni red je torej:
# 
# $\frac{1}{1}, \frac{2}{1}, \frac{1}{2}, \frac{3}{1}, \frac{2}{2}, \frac{1}{3},
# \frac{4}{1}, \frac{3}{2}, \frac{2}{3}, \frac{1}{4}, \ldots$
# 
# Sestavite generator `pozitivna_racionalna()`, ki bo vračal pare števcev in
# imenovalcev pozitivnih racionalnih števil. Vrstni red teh števil naj bo tak,
# kot je opisano zgoraj. Zgled:
# 
#     >>> g = pozitivna_racionalna()
#     >>> [next(g) for i in range(10)]
#     [(1, 1), (2, 1), (1, 2), (3, 1), (1, 3), (4, 1), (3, 2), (2, 3), (1, 4), (5, 1)]
# =============================================================================
import math 
def pozitivna_racionalna():
    d = 1
    while True:
        for stevec in range(d, 0, -1):
            imenovalec = d + 1 - stevec
            if math.gcd(stevec, imenovalec) == 1:
                yield (stevec, imenovalec)
        d += 1
# =====================================================================@009869=
# 3. podnaloga
# Zdaj pa sestavite še generator `racionalna_stevila()`, bo vračal
# racionalna števila.
# 
# Najprej naj vrne število 0, potem pa vsa racionalna števila v enakem
# vrstnem redu kot pri prejšnji podnalogi, pri čemer naj najprej vrne
# pozitivno število, potem pa še ustrezno negativno število. Zgled:
# 
#     >>> g = racionalna_stevila()
#     >>> [next(g) for i in range(10)]
#     [(0, 1), (1, 1), (-1, 1), (2, 1), (-2, 1),
#      (1, 2), (-1, 2), (3, 1), (-3, 1), (1, 3)]
# =============================================================================
def racionalna_stevila():
    yield (0, 1)
    for a, b in pozitivna_racionalna():
        yield (a, b)
        yield (-a, b)




































































































# ============================================================================@

'Če vam Python sporoča, da je v tej vrstici sintaktična napaka,'
'se napaka v resnici skriva v zadnjih vrsticah vaše kode.'

'Kode od tu naprej NE SPREMINJAJTE!'


















































import json, os, re, sys, shutil, traceback, urllib.error, urllib.request


import io, sys
from contextlib import contextmanager

class VisibleStringIO(io.StringIO):
    def read(self, size=None):
        x = io.StringIO.read(self, size)
        print(x, end='')
        return x

    def readline(self, size=None):
        line = io.StringIO.readline(self, size)
        print(line, end='')
        return line


class Check:
    parts = None
    current_part = None
    part_counter = None

    @staticmethod
    def has_solution(part):
        return part['solution'].strip() != ''

    @staticmethod
    def initialize(parts):
        Check.parts = parts
        for part in Check.parts:
            part['valid'] = True
            part['feedback'] = []
            part['secret'] = []

    @staticmethod
    def part():
        if Check.part_counter is None:
            Check.part_counter = 0
        else:
            Check.part_counter += 1
        Check.current_part = Check.parts[Check.part_counter]
        return Check.has_solution(Check.current_part)

    @staticmethod
    def feedback(message, *args, **kwargs):
        Check.current_part['feedback'].append(message.format(*args, **kwargs))

    @staticmethod
    def error(message, *args, **kwargs):
        Check.current_part['valid'] = False
        Check.feedback(message, *args, **kwargs)

    @staticmethod
    def clean(x, digits=6, typed=False):
        t = type(x)
        if t is float:
            x = round(x, digits)
            # Since -0.0 differs from 0.0 even after rounding,
            # we change it to 0.0 abusing the fact it behaves as False.
            v = x if x else 0.0
        elif t is complex:
            v = complex(Check.clean(x.real, digits, typed), Check.clean(x.imag, digits, typed))
        elif t is list:
            v = list([Check.clean(y, digits, typed) for y in x])
        elif t is tuple:
            v = tuple([Check.clean(y, digits, typed) for y in x])
        elif t is dict:
            v = sorted([(Check.clean(k, digits, typed), Check.clean(v, digits, typed)) for (k, v) in x.items()])
        elif t is set:
            v = sorted([Check.clean(y, digits, typed) for y in x])
        else:
            v = x
        return (t, v) if typed else v

    @staticmethod
    def secret(x, hint=None, clean=None):
        clean = Check.get('clean', clean)
        Check.current_part['secret'].append((str(clean(x)), hint))

    @staticmethod
    def equal(expression, expected_result, clean=None, env=None, update_env=None):
        global_env = Check.init_environment(env=env, update_env=update_env)
        clean = Check.get('clean', clean)
        actual_result = eval(expression, global_env)
        if clean(actual_result) != clean(expected_result):
            Check.error('Izraz {0} vrne {1!r} namesto {2!r}.',
                        expression, actual_result, expected_result)
            return False
        else:
            return True

    @staticmethod
    def approx(expression, expected_result, tol=1e-6, env=None, update_env=None):
        try:
            import numpy as np
        except ImportError:
            Check.error('Namestiti morate numpy.')
            return False
        if not isinstance(expected_result, np.ndarray):
            Check.error('Ta funkcija je namenjena testiranju za tip np.ndarray.')

        if env is None:
            env = dict()
        env.update({'np': np})
        global_env = Check.init_environment(env=env, update_env=update_env)
        actual_result = eval(expression, global_env)
        if type(actual_result) is not type(expected_result):
            Check.error("Rezultat ima napačen tip. Pričakovan tip: {}, dobljen tip: {}.",
                        type(expected_result).__name__, type(actual_result).__name__)
            return False
        exp_shape = expected_result.shape
        act_shape = actual_result.shape
        if exp_shape != act_shape:
            Check.error("Obliki se ne ujemata. Pričakovana oblika: {}, dobljena oblika: {}.", exp_shape, act_shape)
            return False
        try:
            np.testing.assert_allclose(expected_result, actual_result, atol=tol, rtol=tol)
            return True
        except AssertionError as e:
            Check.error("Rezultat ni pravilen." + str(e))
            return False

    @staticmethod
    def run(statements, expected_state, clean=None, env=None, update_env=None):
        code = "\n".join(statements)
        statements = "  >>> " + "\n  >>> ".join(statements)
        global_env = Check.init_environment(env=env, update_env=update_env)
        clean = Check.get('clean', clean)
        exec(code, global_env)
        errors = []
        for (x, v) in expected_state.items():
            if x not in global_env:
                errors.append('morajo nastaviti spremenljivko {0}, vendar je ne'.format(x))
            elif clean(global_env[x]) != clean(v):
                errors.append('nastavijo {0} na {1!r} namesto na {2!r}'.format(x, global_env[x], v))
        if errors:
            Check.error('Ukazi\n{0}\n{1}.', statements,  ";\n".join(errors))
            return False
        else:
            return True

    @staticmethod
    @contextmanager
    def in_file(filename, content, encoding=None):
        encoding = Check.get('encoding', encoding)
        with open(filename, 'w', encoding=encoding) as f:
            for line in content:
                print(line, file=f)
        old_feedback = Check.current_part['feedback'][:]
        yield
        new_feedback = Check.current_part['feedback'][len(old_feedback):]
        Check.current_part['feedback'] = old_feedback
        if new_feedback:
            new_feedback = ['\n    '.join(error.split('\n')) for error in new_feedback]
            Check.error('Pri vhodni datoteki {0} z vsebino\n  {1}\nso se pojavile naslednje napake:\n- {2}', filename, '\n  '.join(content), '\n- '.join(new_feedback))

    @staticmethod
    @contextmanager
    def input(content, visible=None):
        old_stdin = sys.stdin
        old_feedback = Check.current_part['feedback'][:]
        try:
            with Check.set_stringio(visible):
                sys.stdin = Check.get('stringio')('\n'.join(content) + '\n')
                yield
        finally:
            sys.stdin = old_stdin
        new_feedback = Check.current_part['feedback'][len(old_feedback):]
        Check.current_part['feedback'] = old_feedback
        if new_feedback:
            new_feedback = ['\n  '.join(error.split('\n')) for error in new_feedback]
            Check.error('Pri vhodu\n  {0}\nso se pojavile naslednje napake:\n- {1}', '\n  '.join(content), '\n- '.join(new_feedback))

    @staticmethod
    def out_file(filename, content, encoding=None):
        encoding = Check.get('encoding', encoding)
        with open(filename, encoding=encoding) as f:
            out_lines = f.readlines()
        equal, diff, line_width = Check.difflines(out_lines, content)
        if equal:
            return True
        else:
            Check.error('Izhodna datoteka {0}\n  je enaka{1}  namesto:\n  {2}', filename, (line_width - 7) * ' ', '\n  '.join(diff))
            return False

    @staticmethod
    def output(expression, content, env=None, update_env=None):
        global_env = Check.init_environment(env=env, update_env=update_env)
        old_stdout = sys.stdout
        sys.stdout = io.StringIO()
        try:
            exec(expression, global_env)
        finally:
            output = sys.stdout.getvalue().rstrip().splitlines()
            sys.stdout = old_stdout
        equal, diff, line_width = Check.difflines(output, content)
        if equal:
            return True
        else:
            Check.error('Program izpiše{0}  namesto:\n  {1}', (line_width - 13) * ' ', '\n  '.join(diff))
            return False

    @staticmethod
    def difflines(actual_lines, expected_lines):
        actual_len, expected_len = len(actual_lines), len(expected_lines)
        if actual_len < expected_len:
            actual_lines += (expected_len - actual_len) * ['\n']
        else:
            expected_lines += (actual_len - expected_len) * ['\n']
        equal = True
        line_width = max(len(actual_line.rstrip()) for actual_line in actual_lines + ['Program izpiše'])
        diff = []
        for out, given in zip(actual_lines, expected_lines):
            out, given = out.rstrip(), given.rstrip()
            if out != given:
                equal = False
            diff.append('{0} {1} {2}'.format(out.ljust(line_width), '|' if out == given else '*', given))
        return equal, diff, line_width

    @staticmethod
    def init_environment(env=None, update_env=None):
        global_env = globals()
        if not Check.get('update_env', update_env):
            global_env = dict(global_env)
        global_env.update(Check.get('env', env))
        return global_env

    @staticmethod
    def generator(expression, expected_values, should_stop=None, further_iter=None, clean=None, env=None, update_env=None):
        from types import GeneratorType
        global_env = Check.init_environment(env=env, update_env=update_env)
        clean = Check.get('clean', clean)
        gen = eval(expression, global_env)
        if not isinstance(gen, GeneratorType):
            Check.error("Izraz {0} ni generator.", expression)
            return False

        try:
            for iteration, expected_value in enumerate(expected_values):
                actual_value = next(gen)
                if clean(actual_value) != clean(expected_value):
                    Check.error("Vrednost #{0}, ki jo vrne generator {1} je {2!r} namesto {3!r}.",
                                iteration, expression, actual_value, expected_value)
                    return False
            for _ in range(Check.get('further_iter', further_iter)):
                next(gen)  # we will not validate it
        except StopIteration:
            Check.error("Generator {0} se prehitro izteče.", expression)
            return False

        if Check.get('should_stop', should_stop):
            try:
                next(gen)
                Check.error("Generator {0} se ne izteče (dovolj zgodaj).", expression)
            except StopIteration:
                pass  # this is fine
        return True

    @staticmethod
    def summarize():
        for i, part in enumerate(Check.parts):
            if not Check.has_solution(part):
                print('{0}. podnaloga je brez rešitve.'.format(i + 1))
            elif not part['valid']:
                print('{0}. podnaloga nima veljavne rešitve.'.format(i + 1))
            else:
                print('{0}. podnaloga ima veljavno rešitev.'.format(i + 1))
            for message in part['feedback']:
                print('  - {0}'.format('\n    '.join(message.splitlines())))

    settings_stack = [{
        'clean': clean.__func__,
        'encoding': None,
        'env': {},
        'further_iter': 0,
        'should_stop': False,
        'stringio': VisibleStringIO,
        'update_env': False,
    }]

    @staticmethod
    def get(key, value=None):
        if value is None:
            return Check.settings_stack[-1][key]
        return value

    @staticmethod
    @contextmanager
    def set(**kwargs):
        settings = dict(Check.settings_stack[-1])
        settings.update(kwargs)
        Check.settings_stack.append(settings)
        try:
            yield
        finally:
            Check.settings_stack.pop()

    @staticmethod
    @contextmanager
    def set_clean(clean=None, **kwargs):
        clean = clean or Check.clean
        with Check.set(clean=(lambda x: clean(x, **kwargs))
                             if kwargs else clean):
            yield

    @staticmethod
    @contextmanager
    def set_environment(**kwargs):
        env = dict(Check.get('env'))
        env.update(kwargs)
        with Check.set(env=env):
            yield

    @staticmethod
    @contextmanager
    def set_stringio(stringio):
        if stringio is True:
            stringio = VisibleStringIO
        elif stringio is False:
            stringio = io.StringIO
        if stringio is None or stringio is Check.get('stringio'):
            yield
        else:
            with Check.set(stringio=stringio):
                yield


def _validate_current_file():
    def extract_parts(filename):
        with open(filename, encoding='utf-8') as f:
            source = f.read()
        part_regex = re.compile(
            r'# =+@(?P<part>\d+)=\s*\n' # beginning of header
            r'(\s*#( [^\n]*)?\n)+?'     # description
            r'\s*# =+\s*?\n'            # end of header
            r'(?P<solution>.*?)'        # solution
            r'(?=\n\s*# =+@)',          # beginning of next part
            flags=re.DOTALL | re.MULTILINE
        )
        parts = [{
            'part': int(match.group('part')),
            'solution': match.group('solution')
        } for match in part_regex.finditer(source)]
        # The last solution extends all the way to the validation code,
        # so we strip any trailing whitespace from it.
        parts[-1]['solution'] = parts[-1]['solution'].rstrip()
        return parts

    def backup(filename):
        backup_filename = None
        suffix = 1
        while not backup_filename or os.path.exists(backup_filename):
            backup_filename = '{0}.{1}'.format(filename, suffix)
            suffix += 1
        shutil.copy(filename, backup_filename)
        return backup_filename

    def submit_parts(parts, url, token):
        submitted_parts = []
        for part in parts:
            if Check.has_solution(part):
                submitted_part = {
                    'part': part['part'],
                    'solution': part['solution'],
                    'valid': part['valid'],
                    'secret': [x for (x, _) in part['secret']],
                    'feedback': json.dumps(part['feedback']),
                }
                if 'token' in part:
                    submitted_part['token'] = part['token']
                submitted_parts.append(submitted_part)
        data = json.dumps(submitted_parts).encode('utf-8')
        headers = {
            'Authorization': token,
            'content-type': 'application/json'
        }
        request = urllib.request.Request(url, data=data, headers=headers)
        # This is a workaround because some clients (and not macOS ones!) report
        # <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: certificate has expired (_ssl.c:1129)>
        import ssl
        context = ssl._create_unverified_context()
        response = urllib.request.urlopen(request, context=context)
        # When the issue is resolved, the following should be used
        # response = urllib.request.urlopen(request)
        return json.loads(response.read().decode('utf-8'))

    def update_attempts(old_parts, response):
        updates = {}
        for part in response['attempts']:
            part['feedback'] = json.loads(part['feedback'])
            updates[part['part']] = part
        for part in old_parts:
            valid_before = part['valid']
            part.update(updates.get(part['part'], {}))
            valid_after = part['valid']
            if valid_before and not valid_after:
                wrong_index = response['wrong_indices'].get(str(part['part']))
                if wrong_index is not None:
                    hint = part['secret'][wrong_index][1]
                    if hint:
                        part['feedback'].append('Namig: {}'.format(hint))


    filename = os.path.abspath(sys.argv[0])
    file_parts = extract_parts(filename)
    Check.initialize(file_parts)

    if Check.part():
        Check.current_part['token'] = 'eyJwYXJ0Ijo5ODY3LCJ1c2VyIjo3MzYzfQ:1nh9Oc:IPhphvo0EBe2H7uJIE8QL_sPCiU'
        try:
            testCases = [("prastevila(1)", [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113], {'further_iter': 100}),
                         ("prastevila(2)", [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113], {'further_iter': 200}),
                         ("prastevila(2013)", [2017, 2027, 2029, 2039, 2053, 2063, 2069, 2081, 2083, 2087, 2089, 2099, 2111, 2113, 2129, 2131, 2137, 2141, 2143, 2153, 2161, 2179, 2203, 2207, 2213, 2221, 2237, 2239, 2243, 2251], {'further_iter': 50}),
                         ("prastevila(1000000)", [1000003, 1000033, 1000037, 1000039, 1000081, 1000099, 1000117, 1000121, 1000133, 1000151, 1000159, 1000171, 1000183, 1000187, 1000193, 1000199, 1000211, 1000213, 1000231, 1000249, 1000253, 1000273, 1000289, 1000291, 1000303, 1000313, 1000333, 1000357, 1000367, 1000381], {'further_iter': 20})]
            for example, correct, options in testCases:
                if not Check.generator(example, correct, **options):
                    break
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        Check.current_part['token'] = 'eyJwYXJ0Ijo5ODY4LCJ1c2VyIjo3MzYzfQ:1nh9Oc:-LnmOt2AlkVImX7PtZyxQR2dnRM'
        try:
            Check.generator("pozitivna_racionalna()", [
                (1, 1), (2, 1), (1, 2), (3, 1), (1, 3),
                (4, 1), (3, 2), (2, 3), (1, 4), (5, 1),
                (1, 5), (6, 1), (5, 2), (4, 3), (3, 4),
                (2, 5), (1, 6), (7, 1), (5, 3), (3, 5),
                (1, 7), (8, 1), (7, 2), (5, 4), (4, 5),
                (2, 7), (1, 8), (9, 1), (7, 3), (3, 7),
                (1, 9), (10, 1), (9, 2), (8, 3), (7, 4),
                (6, 5), (5, 6), (4, 7), (3, 8), (2, 9),
                (1, 10), (11, 1), (7, 5), (5, 7), (1, 11),
                (12, 1), (11, 2), (10, 3), (9, 4), (8, 5),
                (7, 6), (6, 7), (5, 8), (4, 9), (3, 10),
                (2, 11), (1, 12), (13, 1), (11, 3), (9, 5),
                (5, 9), (3, 11), (1, 13), (14, 1), (13, 2),
                (11, 4), (8, 7), (7, 8), (4, 11), (2, 13),
                (1, 14), (15, 1), (13, 3), (11, 5), (9, 7),
                (7, 9), (5, 11), (3, 13), (1, 15), (16, 1),
                (15, 2), (14, 3), (13, 4), (12, 5), (11, 6),
                (10, 7), (9, 8), (8, 9), (7, 10), (6, 11),
                (5, 12), (4, 13), (3, 14), (2, 15), (1, 16),
                (17, 1), (13, 5), (11, 7), (7, 11), (5, 13)
            ], further_iter=1000)
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        Check.current_part['token'] = 'eyJwYXJ0Ijo5ODY5LCJ1c2VyIjo3MzYzfQ:1nh9Oc:bIe6yTUc123avj7Zns7NfFSA21E'
        try:
            Check.generator("racionalna_stevila()", [
                (0, 1), (1, 1), (-1, 1), (2, 1), (-2, 1),
                (1, 2), (-1, 2), (3, 1), (-3, 1), (1, 3),
                (-1, 3), (4, 1), (-4, 1), (3, 2), (-3, 2),
                (2, 3), (-2, 3), (1, 4), (-1, 4), (5, 1),
                (-5, 1), (1, 5), (-1, 5), (6, 1), (-6, 1),
                (5, 2), (-5, 2), (4, 3), (-4, 3), (3, 4),
                (-3, 4), (2, 5), (-2, 5), (1, 6), (-1, 6),
                (7, 1), (-7, 1), (5, 3), (-5, 3), (3, 5),
                (-3, 5), (1, 7), (-1, 7), (8, 1), (-8, 1),
                (7, 2), (-7, 2), (5, 4), (-5, 4), (4, 5),
                (-4, 5), (2, 7), (-2, 7), (1, 8), (-1, 8),
                (9, 1), (-9, 1), (7, 3), (-7, 3), (3, 7),
                (-3, 7), (1, 9), (-1, 9), (10, 1), (-10, 1),
                (9, 2), (-9, 2), (8, 3), (-8, 3), (7, 4),
                (-7, 4), (6, 5), (-6, 5), (5, 6), (-5, 6),
                (4, 7), (-4, 7), (3, 8), (-3, 8), (2, 9),
                (-2, 9), (1, 10), (-1, 10), (11, 1), (-11, 1),
                (7, 5), (-7, 5), (5, 7), (-5, 7), (1, 11),
                (-1, 11), (12, 1), (-12, 1), (11, 2), (-11, 2),
                (10, 3), (-10, 3), (9, 4), (-9, 4), (8, 5)
            ], further_iter=1000)
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    print('Shranjujem rešitve na strežnik... ', end="")
    try:
        url = 'https://www.projekt-tomo.si/api/attempts/submit/'
        token = 'Token a5b410e095ee2269944840206d6a76b4f6ad0115'
        response = submit_parts(Check.parts, url, token)
    except urllib.error.URLError:
        message = ('\n'
                   '-------------------------------------------------------------------\n'
                   'PRI SHRANJEVANJU JE PRIŠLO DO NAPAKE!\n'
                   'Preberite napako in poskusite znova ali se posvetujte z asistentom.\n'
                   '-------------------------------------------------------------------\n')
        print(message)
        traceback.print_exc()
        print(message)
        sys.exit(1)
    else:
        print('Rešitve so shranjene.')
        update_attempts(Check.parts, response)
        if 'update' in response:
            print('Updating file... ', end="")
            backup_filename = backup(filename)
            with open(__file__, 'w', encoding='utf-8') as f:
                f.write(response['update'])
            print('Previous file has been renamed to {0}.'.format(backup_filename))
            print('If the file did not refresh in your editor, close and reopen it.')
    Check.summarize()

if __name__ == '__main__':
    _validate_current_file()
