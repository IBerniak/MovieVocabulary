from pysrt import open as opening
import nltk
from nltk.stem import WordNetLemmatizer

list_500_words = ('a', 'able', 'about', 'accept', 'across', 'act', 'action', 'activity', 'actually',
                  'add', 'after', 'again', 'against', 'age', 'ago', 'agree', 'all', 'allow', 'almost', 'already',
                  'also', 'although', 'always', 'american', 'among', 'an', 'and', 'another', 'any', 'anything',
                  'appear', 'area',
                  'arm', 'around', 'art', 'as', 'ask', 'at', 'authority', 'available', 'away', 'back', 'bad', 'bank',
                  'be', 'because', 'become', 'before', 'begin', 'behind', 'believe', 'between', 'big', 'bit', 'black',
                  'body', 'book', 'both', 'boy', 'bring', 'build', 'building', 'business', 'but', 'buy', 'by', 'call',
                  'can', 'car', 'carry', 'case', 'cause', 'centre', 'century', 'certain', 'change', 'child', 'church',
                  'city', 'class', 'clear', 'club', 'come', 'committee', 'community', 'company', 'condition',
                  'consider', 'continue', 'control', 'cost', 'could', 'council', 'country', 'course', 'court', 'create',
                  'daddy', 'day', 'death', 'decide', 'decision', 'department', 'describe', 'develop', 'development',
                  'die', 'different', 'difficult', 'do', 'door', 'down', 'draw', 'during', 'each', 'early', 'economic',
                  'education', 'effect', 'else', 'end', 'enough', 'even', 'event', 'ever', 'every', 'evidence',
                  'example', 'expect', 'experience', 'eye', 'face', 'fact', 'fall', 'family', 'far', 'father', 'feel',
                  'few', 'figure', 'find', 'five', 'follow', 'food', 'foot', 'for', 'force', 'form', 'four', 'friend',
                  'from', 'full', 'further', 'game', 'general', 'get', 'girl', 'give', 'go', 'good', 'government',
                  'great', 'ground', 'group', 'half', 'hand', 'happen', 'have', 'he', 'head', 'health', 'hear', 'help',
                  'her', 'here', 'high', 'him', 'himself', 'his', 'history', 'hold', 'home', 'hope', 'hour', 'house',
                  'how', 'however', 'i', 'idea', 'if', 'important', 'in', 'include', 'including', 'increase',
                  'industry', 'information', 'interest', 'international', 'into', 'involve', 'issue', 'it', 'its',
                  'itself', 'job', 'just', 'keep', 'kind', 'know', 'land', 'language', 'large', 'last', 'late', 'later',
                  'law', 'lead', 'learn', 'least', 'leave', 'less', 'let', 'letter', 'level', 'lie', 'life', 'like',
                  'likely', 'line', 'little', 'live', 'local', 'long', 'look', 'lose', 'lot', 'low', 'main', 'major',
                  'make', 'man', 'management', 'many', 'market', 'matter', 'may', 'me', 'mean', 'meet', 'meeting',
                  'member', 'might', 'million', 'mind', 'minister', 'minute', 'moment', 'mommy', 'money', 'month',
                  'more', 'morning', 'most', 'mother', 'move', 'mr', 'much', 'mum', 'mummy', 'must', 'my', 'name',
                  'national',
                  'need', 'never', 'new', 'next', 'night', 'no', 'no', 'no', 'no', 'no', 'no', 'not', 'nothing', 'now',
                  'number', 'of', 'off', 'offer', 'office', 'often', 'oh', 'old', 'on', 'once', 'one', 'only', 'open',
                  'or', 'order', 'other', 'others', 'our', 'out', 'over', 'own', 'paper', 'parent', 'part',
                  'particular', 'particularly', 'party', 'pass', 'patient', 'pay', 'people', 'percent', 'perhaps',
                  'period', 'person', 'place', 'plan', 'play', 'point', 'police', 'policy', 'political', 'position',
                  'possible', 'power', 'practice', 'price', 'probably', 'problem', 'process', 'produce', 'product',
                  'programme', 'provide', 'public', 'put', 'question', 'quite', 'range', 'rate', 'rather', 'reach',
                  'read', 'real', 'really', 'reason', 'receive', 'remain', 'remember', 'report', 'require', 'research',
                  'result', 'return', 'right', 'road', 'role', 'room', 'run', 'same', 'say', 'school', 'section', 'see',
                  'seem', 'sell', 'send', 'sense', 'service', 'set', 'several', 'shall', 'she', 'should', 'show',
                  'side', 'since', 'sit', 'situation', 'six', 'small', 'so', 'social', 'society', 'some', 'something',
                  'sometimes', 'soon', 'sooner', 'sort', 'speak', 'special', 'spend', 'staff', 'stage', 'stand',
                  'start', 'state', 'still', 'stop', 'student', 'study', 'subject', 'such', 'suggest', 'support',
                  'sure', 'system', 'table', 'take', 'talk', 'teacher', 'team', 'tell', 'term', 'than', 'that', 'the',
                  'their', 'them', 'themselves', 'then', 'there', 'therefore', 'these', 'they', 'thing', 'think',
                  'this', 'those', 'though', 'three', 'through', 'thus', 'time', 'to', 'today', 'together', 'too',
                  'towards', 'town', 'trade', 'try', 'turn', 'two', 'type', 'unbelievable', 'under', 'understand',
                  'until', 'up', 'upon', 'us', 'use', 'value', 'very', 'view', 'voice', 'walk', 'want', 'war', 'watch',
                  'water', 'way', 'we', 'week', 'well', 'what', 'when', 'where', 'whether', 'which', 'while', 'white',
                  'who', 'whose', 'why', 'will', 'win', 'with', 'within', 'without', 'woman', 'word', 'work', 'world',
                  'would', 'write', 'yeah', 'year', 'yes', 'yet', 'you', 'young', 'your')

added_list_1000_words = ('America', 'Britain', 'Christ', 'Europe', 'France', 'Germany', 'Mrs', 'PM', 'TV', 'ability',
                         'above', 'access', 'according', 'account', 'achieve', 'addition', 'admit', 'advantage',
                         'advice', 'affair', 'affect', 'agreement', 'air', 'along', 'amount', 'analysis', 'animal',
                         'announce', 'answer', 'anyhow', 'anyone', 'anyway', 'apart', 'appeal', 'application', 'apply',
                         'approach', 'appropriate', 'approximate', 'argue', 'argument', 'army', 'arrive', 'article',
                         'aspect', 'association', 'assume', 'attack', 'attempt', 'attention', 'attitude', 'avoid',
                         'award', 'aware', 'baby', 'bar', 'base', 'basic', 'basis', 'bear', 'bed', 'beforehand',
                         'behaviour', 'benefit', 'best', 'better', 'beyond', 'bill', 'billion', 'blood', 'board',
                         'boiling', 'bound', 'box', 'break', 'brother', 'butcher', 'campaign', 'capital', 'card',
                         'care', 'catch', 'cell', 'cellphone', 'cent', 'central', 'certainly', 'chair', 'chance',
                         'chapter', 'character', 'charge', 'choice', 'choose', 'circumstance', 'claim', 'clearly',
                         'client', 'close', 'collection', 'colour', 'commission', 'common', 'compare', 'competition',
                         'complete', 'computer', 'concern', 'concerned', 'conference', 'considerable', 'contain',
                         'context', 'contract', 'converse', 'cos', 'county', 'couple', 'cover', 'culture', 'cup',
                         'current', 'customer', 'cut', 'dark', 'data', 'date', 'daughter', 'dead', 'deal', 'defence',
                         'degree', 'demand', 'depend', 'design', 'despite', 'detail', 'determine', 'difference',
                         'difficulty', 'direct', 'direction', 'director', 'discover', 'discuss', 'discussion',
                         'disease', 'division', 'doctor', 'dog', 'doubt', 'drive', 'drop', 'due', 'duty', 'easily',
                         'easy', 'eat', 'economy', 'effective', 'effort', 'eight', 'either', 'election', 'element',
                         'employment', 'enable', 'encourage', 'energy', 'enjoy', 'ensure', 'enter', 'environment',
                         'especially', 'establish', 'evening', 'everyone', 'everything', 'exactly', 'exist', 'explain',
                         'express', 'extent', 'facility', 'factor', 'fail', 'feature', 'feeling', 'field', 'fight',
                         'fill', 'film', 'final', 'finally', 'financial', 'fine', 'finish', 'fire', 'firm', 'fish',
                         'floor', 'fly', 'following', 'foreign', 'forget', 'former', 'forward', 'free', 'front',
                         'function', 'fund', 'future', 'garden', 'generally', 'glass', 'goal', 'grow', 'growth',
                         'hair', 'happy', 'hard', 'heart', 'heavy', 'herself', 'hit', 'holiday', 'horse', 'hospital',
                         'hotel', 'hullo', 'human', 'hundred', 'husband', 'identify', 'image', 'immediately',
                         'importance', 'improve', 'income', 'indeed', 'indicate', 'individual', 'industrial',
                         'instance', 'instead', 'institution', 'intend', 'interesting', 'introduce', 'investment',
                         'item', 'join', 'kill', 'king', 'knowledge', 'labour', 'lady', 'leader', 'left', 'leg',
                         'legal', 'library', 'light', 'list', 'listen', 'loss', 'love', 'machine', 'maintain',
                         'majority', 'manage', 'manager', 'material', 'maybe', 'means', 'measure', 'memory', 'mention',
                         'method', 'mile', 'military', 'miss', 'model', 'modern', 'mouth', 'movement', 'music',
                         'myself', 'natural', 'nature', 'near', 'nearly', 'necessary', 'news', 'nice', 'no', 'nor',
                         'normal', 'note', 'notice', 'object', 'obtain', 'obviously', 'occur', 'officer', 'oil',
                         'okay', 'operate', 'operation', 'opportunity', 'organisation', 'original', 'outside', 'page',
                         'parliament', 'pattern', 'payment', 'per', 'performance', 'personal', 'photocopy', 'pick',
                         'picture', 'piece', 'plant', 'player', 'please', 'poor', 'popular', 'population', 'post',
                         'pound', 'prepare', 'present', 'president', 'press', 'pressure', 'prevent', 'previous',
                         'prime', 'principle', 'private', 'procedure', 'production', 'professional', 'profit',
                         'project', 'property', 'proposal', 'prove', 'provision', 'publish', 'pull', 'pupil',
                         'purpose', 'quality', 'quickly', 'raise', 'ready', 'recent', 'recently', 'record', 'red',
                         'reduce', 'refer', 'reference', 'reflect', 'refuse', 'regard', 'region', 'relate', 'relation',
                         'relationship', 'remove', 'replace', 'represent', 'resource', 'respect', 'response',
                         'responsibility', 'rest', 'reveal', 'rise', 'risk', 'round', 'royal', 'rule', 'sale', 'save',
                         'scheme', 'science', 'sea', 'season', 'seat', 'secretary', 'sector', 'security', 'seek',
                         'series', 'serious', 'serve', 'seven', 'share', 'shop', 'short', 'sign', 'significant',
                         'similar', 'simple', 'simply', 'single', 'site', 'size', 'skill', 'smile', 'someone', 'son',
                         'sorry', 'sound', 'source', 'space', 'specific', 'stairs', 'standard', 'statement', 'station',
                         'stay', 'step', 'stone', 'story', 'street', 'strong', 'structure', 'style', 'success',
                         'successful', 'suddenly', 'suffer', 'summer', 'suppose', 'surface', 'survey', 'task', 'tax',
                         'teach', 'technique', 'technology', 'television', 'ten', 'tend', 'terms', 'test', 'text',
                         'thank', 'theory', 'third', 'thought', 'thousand', 'throughout', 'throw', 'title', 'top',
                         'total', 'traditional', 'train', 'training', 'treat', 'treatment', 'tree', 'trouble', 'true',
                         'union', 'unit', 'university', 'unless', 'used', 'useful', 'user', 'usually', 'variety',
                         'various', 'version', 'village', 'visit', 'wait', 'wall', 'wear', 'website', 'whatever',
                         'whole', 'whom', 'wide', 'wife', 'window', 'windy', 'wish', 'wonder', 'worker', 'wrong',
                         'yesterday', 'yourself')

added_list_1500_words = ('Africa', 'African', 'April', 'Australia', 'Australian', 'British', 'China', 'Chinese',
                         'Christian', 'Christmas', 'December', 'Egypt', 'Egyptian', 'European', 'February', 'French',
                         'Indian', 'Internet', 'Italy', 'January', 'Japan', 'Jesus', 'July', 'June', 'Ms', 'November',
                         'October', 'Paris', 'Russia', 'Scotland', 'Scottish', 'September', 'Spain', 'Swiss',
                         'accident', 'acquire', 'active', 'actual', 'additional', 'administration', 'adopt', 'adult',
                         'afternoon', 'agency', 'agent', 'ahead', 'aid', 'aim', 'alone', 'annual', 'anti', 'apparently',
                         'appearance', 'appoint', 'apropos', 'arise', 'arrange', 'arrangement', 'artist', 'assessment',
                         'associate', 'attend', 'attorney', 'attract', 'audience', 'august', 'author', 'background',
                         'bag', 'balance', 'ball', 'band', 'baseball', 'battle', 'beat', 'beautiful', 'beginning',
                         'belief', 'below', 'bind', 'bird', 'blue', 'boat', 'born', 'branch', 'broad', 'budget', 'bus',
                         'cabinet', 'candidate', 'career', 'carefully', 'cash', 'category', 'chairman', 'check',
                         'cherry', 'chief', 'chuck', 'civil', 'clothe', 'clothes', 'coffee', 'cold', 'colleague',
                         'collect', 'college', 'comment', 'commercial', 'commit', 'commitment', 'communication',
                         'completely', 'complex', 'concentrate', 'concept', 'conclusion', 'confidence', 'confirm',
                         'conflict', 'connection', 'consequence', 'consideration', 'construction', 'consumer',
                         'contact', 'content', 'contrast', 'contribution', 'conversation', 'cooker', 'copy', 'corner',
                         'crap', 'credit', 'crime', 'crisis', 'cross', 'cry', 'cultural', 'currently', 'daft', 'damage',
                         'danger', 'debate', 'debt', 'deep', 'define', 'demonstrate', 'deny', 'description', 'dinner',
                         'directly', 'disgusting', 'distance', 'distribution', 'district', 'document', 'dole',
                         'domestic', 'drink', 'driver', 'drug', 'dye', 'earth', 'edge', 'emerge', 'employ', 'employee',
                         'employer', 'engine', 'entirely', 'entry', 'environmental', 'equally', 'equipment', 'especial',
                         'essential', 'estate', 'eventually', 'examine', 'excellent', 'except', 'exchange', 'executive',
                         'exercise', 'exhibition', 'existence', 'existing', 'explanation', 'expression', 'extend',
                         'extra', 'extremely', 'failure', 'fair', 'fairly', 'famous', 'farm', 'farmer', 'fear', 'file',
                         'filthy', 'finger', 'firms', 'fit', 'flower', 'ford', 'forest', 'formal', 'frank', 'freedom',
                         'freeway', 'freezer', 'fresh', 'friday', 'fry', 'fully', 'gain', 'gambling', 'gas', 'gee',
                         'generation', 'gentleman', 'goodbye', 'goods', 'gorgeous', 'gosh', 'gram', 'grant', 'green',
                         'hall', 'handbag', 'hang', 'hardly', 'harry', 'heater', 'heather', 'heck', 'highly', 'hole',
                         'hot', 'housing', 'huge', 'ignore', 'imagine', 'impact', 'impose', 'impossible', 'improvement',
                         'increasingly', 'independent', 'influence', 'injury', 'inside', 'insist', 'insurance',
                         'interested', 'internal', 'intriguing', 'introduction', 'investigation', 'island', 'jack',
                         'joint', 'judge', 'key', 'kitchen', 'lack', 'largely', 'latter', 'laugh', 'launch', 'lay',
                         'league', 'legislation', 'length', 'lift', 'limit', 'link', 'lip', 'living', 'loan', 'lovely',
                         'mainly', 'male', 'manner', 'mar', 'mark', 'marriage', 'marry', 'master', 'match', 'meal',
                         'meaning', 'media', 'medical', 'merely', 'message', 'middle', 'monday', 'museum', 'nation',
                         'network', 'nevertheless', 'newspaper', 'nick', 'nine', 'no', 'non', 'none', 'normally',
                         'north', 'nuclear', 'objective', 'observe', 'obvious', 'occasion', 'official', 'one',
                         'opinion', 'opposition', 'option', 'ordinary', 'otherwise', 'outrage', 'owner', 'package',
                         'pain', 'painting', 'pair', 'paperwork', 'partner', 'past', 'path', 'peace', 'perform', 'phone',
                         'physical', 'planning', 'plus', 'politic', 'politics', 'positive', 'possibility', 'possibly',
                         'potential', 'powerful', 'practical', 'prefer', 'presence', 'previously', 'primary', 'prison',
                         'progress', 'promise', 'proper', 'proportion', 'protect', 'protection', 'push', 'quarter',
                         'race', 'radio', 'railway', 'reaction', 'reader', 'reality', 'reform', 'regional', 'regular',
                         'regulation', 'relatively', 'release', 'relevant', 'relief', 'religious', 'repeat', 'reply',
                         'requirement', 'respond', 'responsible', 'review', 'rich', 'ring', 'river', 'rock', 'route',
                         'safe', 'safety', 'sample', 'saturday', 'scale', 'scene', 'second', 'senior', 'sentence',
                         'separate', 'session', 'settle', 'sex', 'sexual', 'shake', 'shape', 'sheet', 'ship', 'shoot',
                         'shoulder', 'sight', 'sir', 'sister', 'skin', 'sleep', 'slightly', 'slowly', 'soft', 'software',
                         'solution', 'somebody', 'somewhere', 'song', 'south', 'speaker', 'species', 'speech', 'speed',
                         'spirit', 'sport', 'star', 'stare', 'status', 'stick', 'stock', 'straight', 'strange',
                         'strategy', 'strength', 'strike', 'studio', 'stuff', 'sun', 'sunday', 'supply', 'surely',
                         'survive', 'tab', 'target', 'tea', 'technical', 'telephone', 'thirteen', 'threat', 'threaten',
                         'thursday', 'tomorrow', 'tonight', 'touch', 'track', 'tradition', 'traffic', 'transport',
                         'travel', 'trial', 'trust', 'truth', 'tuesday', 'un', 'unable', 'understanding', 'usual',
                         'vary', 'vehicle', 'vice', 'victim', 'victorian', 'video', 'visitor', 'volume', 'vote', 'wage',
                         'warm', 'warn', 'wednesday', 'weekend', 'weight', 'west', 'western', 'wind', 'wine', 'winter',
                         'wood', 'working', 'works', 'worry', 'worth', 'writer', 'yard')

added_list_2000_words = ('Catholic', 'Easter', 'English', 'German', 'Holland', 'Iraqi', 'Japanese', 'Jewish', 'Lord',
                         'Russian', 'Scots', 'Sweden', 'Switzerland', 'Wales', 'absence', 'absolutely', 'academic',
                         'accompany', 'acid', 'ad', 'addicted', 'addiction', 'address', 'advance', 'advise', 'afford',
                         'afraid', 'aircraft', 'alright', 'alternative', 'ancient', 'anybody', 'anymore', 'apparent',
                         'appointment', 'approve', 'assembly', 'assess', 'asset', 'assumption', 'atmosphere', 'attach',
                         'attractive', 'average', 'aye', 'basketball', 'bedroom', 'belong', 'beneath', 'beside',
                         'birth', 'block', 'bloody', 'bloom', 'blow', 'bone', 'border', 'bottle', 'bottom', 'brain',
                         'breath', 'bridge', 'brief', 'bright', 'burn', 'bust', 'busy', 'buzz', 'bypass', 'camel',
                         'capable', 'capacity', 'careful', 'carol', 'cat', 'cement', 'chain', 'challenge', 'channel',
                         'characteristic', 'cheap', 'chemical', 'circle', 'clean', 'climb', 'closely', 'coal', 'code',
                         'combination', 'combine', 'comparison', 'component', 'concentration', 'conclude', 'conduct',
                         'congratulation', 'congress', 'conservative', 'consist', 'constant', 'contribute',
                         'convention', 'correct', 'count', 'crappy', 'creation', 'criminal', 'criterion', 'critical',
                         'criticism', 'crowd', 'curriculum', 'dad', 'dangerous', 'decade', 'declare', 'defendant',
                         'definition', 'deliver', 'democratic', 'deputy', 'derive', 'desire', 'desk', 'destroy',
                         'detailed', 'device', 'dial', 'dialect', 'digest', 'disappear', 'discipline', 'disgust',
                         'display', 'distinction', 'divide', 'double', 'drawing', 'dream', 'dress', 'dry', 'ear',
                         'earn', 'east', 'editor', 'educational', 'effectively', 'egg', 'elderly', 'elsewhere',
                         'emphasis', 'empty', 'enemy', 'engineering', 'enterprise', 'entire', 'entitle', 'equal',
                         'error', 'escape', 'establishment', 'estimate', 'everybody', 'ex', 'examination',
                         'expenditure', 'expense', 'expensive', 'experiment', 'expert', 'external', 'factory',
                         'faith', 'familiar', 'fashion', 'fast', 'favour', 'fee', 'female', 'finance', 'finding',
                         'first', 'fix', 'flat', 'flight', 'flow', 'flu', 'focus', 'football', 'foundation', 'fourth',
                         'frequently', 'frost', 'fruit', 'fuel', 'funny', 'gamble', 'gate', 'gather', 'generate', 'god',
                         'gold', 'greatest', 'greed', 'greedy', 'grey', 'growing', 'guest', 'guide', 'gun', 'handle',
                         'hate', 'heat', 'hell', 'hence', 'hide', 'hill', 'historical', 'hood', 'hop', 'hopeless',
                         'household', 'hurt', 'idiot', 'ignorant', 'illustrate', 'immediate', 'implicate',
                         'implication', 'imply', 'impression', 'incident', 'increased', 'index', 'influenza', 'inform',
                         'initial', 'initiative', 'institute', 'instruction', 'instrument', 'insult', 'intention',
                         'interpretation', 'interstate', 'interview', 'investigate', 'invite', 'iron', 'irritating',
                         'journey', 'jump', 'jumper', 'justice', 'kid', 'knee', 'lawyer', 'leadership', 'leading',
                         'leaf', 'lean', 'liability', 'liberal', 'limited', 'literal', 'literature', 'litter',
                         'location', 'lots', 'luckily', 'lunch', 'madam', 'magazine', 'map', 'married', 'marvel',
                         'mass', 'meanwhile', 'mechanism', 'membership', 'mental', 'messy', 'metal', 'milk', 'mine',
                         'mini', 'ministry', 'mistake', 'mock', 'module', 'mom', 'motion', 'motor', 'mountain',
                         'murder', 'naive', 'narrow', 'naughty', 'necessarily', 'neck', 'negotiation', 'neighbour',
                         'neither', 'niece', 'nil', 'no', 'nobody', 'nod', 'noise', 'nope', 'northern', 'nose',
                         'notion', 'nurse', 'observation', 'offence', 'onto', 'op', 'origin', 'ought', 'ounce',
                         'outcome', 'output', 'outrageous', 'overall', 'overhead', 'overtime', 'panel', 'pants',
                         'park', 'partly', 'passage', 'pathetic', 'pension', 'perfect', 'persuade', 'phase',
                         'photograph', 'plate', 'pleasure', 'plenty', 'pocket', 'pool', 'potter', 'prepared',
                         'pretty', 'priority', 'program', 'promote', 'properly', 'prospect', 'provided', 'pub',
                         'publication', 'quick', 'quiet', 'racing', 'rain', 'rare', 'reading', 'realize', 'reasonable',
                         'recall', 'recognition', 'recognize', 'recommend', 'recover', 'reduction', 'reject',
                         'relative', 'religion', 'rely', 'remind', 'representation', 'representative', 'request',
                         'reside', 'restaurant', 'retain', 'revenue', 'revolt', 'revolution', 'ride', 'roll', 'rome',
                         'roof', 'row', 'rural', 'satisfy', 'scientific', 'scientist', 'score', 'scout', 'screen',
                         'search', 'secondary', 'secure', 'select', 'selection', 'sequence', 'seriously', 'servant',
                         'settlement', 'severe', 'shoe', 'shot', 'shout', 'shut', 'signal', 'significance', 'silence',
                         'sing', 'sky', 'slash', 'slip', 'slow', 'smack', 'sod', 'soil', 'soldier', 'solicitor',
                         'somewhat', 'spot', 'spread', 'spring', 'steal', 'store', 'strongly', 'sub', 'substantial',
                         'succeed', 'sufficient', 'suggestion', 'suitable', 'sum', 'surprise', 'surround', 'switch',
                         'tall', 'tape', 'teaching', 'tear', 'temperature', 'terrible', 'thanks', 'theatre', 'theme',
                         'thin', 'thrill', 'thrilled', 'thriller', 'thy', 'ticket', 'tiny', 'token', 'tone', 'tool',
                         'tooth', 'tory', 'totally', 'tour', 'transfer', 'treaty', 'trend', 'trip', 'troop', 'twice',
                         'typical', 'undertake', 'unemployment', 'unfortunately', 'united', 'unlikely', 'upper',
                         'urban', 'variation', 'vast', 'via', 'victory', 'violence', 'vision', 'vital', 'wash', 'wave',
                         'weapon', 'weather', 'wed', 'welcome', 'welfare', 'whereas', 'whilst', 'widely', 'wild',
                         'wing', 'winner', 'wonderful', 'wreck', 'writing', 'youth')

class VocabularyWord:

    def __init__(self, base_form, form, subtitle_list):
        self.base_form = base_form
        self.forms = dict()
        self.add_form(form, subtitle_list)

        self.flag = 'undefined'
        self.links = {'Dict': None, 'Google': None, 'Images': None}


    def __iter__(self):
        return iter(self.forms)

    def add_form(self, form, subtitle_list):
        self.forms[form] = [sentence for sentence in subtitle_list if
                            ' ' + form + ' ' in sentence
                            or "'" + form + ' ' in sentence
                            or ' ' + form + "'" in sentence]

    # def check_flag(self, person_vocabulary):
    #     if self.base_form in person_vocabulary:
    #         self.flag = 'known'
    #     elif self.base_form in list_500_words:
    #         self.flag = '500'
    #     elif self.base_form in added_list_1000_words:
    #         self.flag = '1000'
    #     elif self.base_form in added_list_1500_words:
    #         self.flag = '1500'
    #     elif self.base_form in added_list_2000_words:
    #         self.flag = '2000'
    #     else:
    #         self.flag = 'new'

    def get_links(self):
        pass

    def __repr__(self):
        return self.base_form


class VocabularyOfMovie:

    def __init__(self, movie_title, movie_year, srt_file):

        lemmatizer = WordNetLemmatizer()

        subs = opening(srt_file)

        self.subtitle_list = [i.text for i in subs]
        self.full_text = ''
        for line in self.subtitle_list:
            self.full_text = self.full_text + '\n' + line

        punctuations = "?:!.,;[]\n-"
        sentence_words = {i for i in nltk.word_tokenize(self.full_text) if not i in punctuations}
        print(sentence_words)

        self.all_words = {}

        for word in sentence_words:
            base_form = lemmatizer.lemmatize(word, pos="v")
            if base_form.startswith("'") or base_form.isdigit():
                continue
            elif base_form in self.all_words:
                temp = self.all_words[base_form]
                temp.add_form(word, self.subtitle_list)
            else:
                self.all_words[base_form] = VocabularyWord(base_form, word, self.subtitle_list)

        self.movie_title = movie_title
        self.movie_year = movie_year

    def __iter__(self):
        return iter(self.all_words)

    def __repr__(self):
        pass

# TO-DO:
# - Correct get_base_form function to receive correct base form for most words
# - Implement logic for the correct case of symbols
# - Define check_flag method
# - Define __repr__ method of VocabularyOfMovie class
# - Define __getitem__ method of VocabularyOfMovie class
# - Define __repr__ method of VocabularyWord class
