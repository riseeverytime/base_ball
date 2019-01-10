import pytest
import matplotlib
matplotlib.use('Agg')

from .utils import *

from stats import pitching

@pytest.mark.test_select_all_plays_module3
def test_select_all_plays_module3():
    assert 'plays:games:games:type:play' in get_assignments(pitching), ''

@pytest.mark.test_select_all_strike_outs_module3
def test_select_all_strike_outs_module3():
    assert 'strike_outs:plays:plays:event:str:contains:K' in get_assignments(pitching), ''

@pytest.mark.test_group_by_year_and_game_module3
def test_group_by_year_and_game_module3():
    assert 'strike_outs:strike_outs:groupby:year:game_id:size' in get_assignments(pitching), ''

@pytest.mark.test_reset_index_module3
def test_reset_index_module3():
    assert 'strike_outs:strike_outs:reset_index:name:strike_outs' in get_assignments(pitching), ''

@pytest.mark.test_apply_an_operation_to_multiple_columns_module3
def test_apply_an_operation_to_multiple_columns_module3():
    assert 'strike_outs:strike_outs:loc:None:None:None:year:strike_outs:apply:pd:to_numeric' in get_assignments(pitching), ''

@pytest.mark.test_change_plot_formatting_module3
def test_change_plot_formatting_module3():
    assert 'strike_outs:plot:x:year:y:strike_outs:kind:scatter:legend:Strike Outs' in get_calls(pitching), ''
    assert 'plt:show' in get_calls(pitching), ''
